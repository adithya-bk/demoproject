import razorpay
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from cart.models import Cart,Order_Details,Payment
from django.views.decorators.csrf import csrf_exempt
from shop.models import Product
from django.views.generic import View
# from cart.models import Order_Details
# Create your views here.
@login_required
def addtocart(request,i):
    u=request.user
    p=Product.objects.get(id=i)
    try:
        c=Cart.objects.get(user=u,product=p)  #retrieving user and product info from Cart table if already exists
        if(p.stock>0):
            c.quantity=c.quantity+1
            c.save()
            p.stock=p.stock-1
            p.save()
    except:
        if(p.stock>0):
            c=Cart.objects.create(user=u,product=p,quantity=1)
            c.save()
            p.stock=p.stock-1
            p.save()
    return redirect('cart:cartview')

@login_required()
def cartview(request):
    u=request.user
    c=Cart.objects.filter(user=u)
    total=0
    for i in c:
        total=total+i.product.price*i.quantity
    context={'cart':c,'total':total}
    return render(request,'cart.html',context)

def cartdecrement(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity>1):
            cart.quantity=cart.quantity-1
            cart.save()
            p.stock=p.stock+1
            p.save()
        else:
            cart.delete()
            p.stock=p.stock+1
            p.save()
    except:
        pass
    return redirect('cart:cartview')

def cartdelete(request,i):
    p = Product.objects.get(id=i)
    u = request.user
    try:
        cart=Cart.objects.get(user=u, product=p)
        cart.delete()
        p.stock=p.stock+cart.quantity
        p.save()
    except:
        pass
    return redirect('cart:cartview')

def orderform(request):
    if(request.method=="POST"):
        a=request.POST['a']
        phone=request.POST['ph']
        pi=request.POST['pin']
        u=request.user
        c=Cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.quantity*i.product.price
        total=int(total)
        # print(total)

        client=razorpay.Client(auth=('rzp_test_TPvy7JAPEsX7Id','0jFxJ0oiZKjxdg5zHvhkmvH6'))
        response_payment=client.order.create(dict(amount=total*100,currency='INR'))
        print(response_payment)
        order_id=response_payment['id']
        status=response_payment['status']
        if(status=='created'):
            p = Payment.objects.create(name=u.username, amount=total, order_id=order_id)
            p.save()
            for i in c:
                o = Order_Details.objects.create(product=i.product, user=i.user, phone=phone, address=a, pin=pi,
                                                order_id=order_id, no_of_items=i.quantity)
                o.save()
            context={'payment':response_payment,'name':u.username}
            return render(request,'payment.html',context)

    return render(request,'orderform.html')
@csrf_exempt
def paymentstatus(request,k):
    user=User.objects.get(username=k)
    login(request,user)
    response=request.POST
    print(response)
    param_dict={
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    client=razorpay.Client(auth=('rzp_test_TPvy7JAPEsX7Id','0jFxJ0oiZKjxdg5zHvhkmvH6'))
    try:
        status=client.utility.verify_payment_signature(param_dict)
        print(status)
        m=Payment.objects.get(order_id=response['razorpay_order_id'])
        m.paid=True
        m.razorpay_payment_id=response['razorpay_payment_id']
        m.save()
        o=Order_Details.objects.filter(order_id=response['razorpay_order_id'])
        for i in o:
            i.payment_status="Completed"
            i.save()
        c=Cart.objects.filter(user=user)
        c.delete()


    except:
        pass

    return render(request,'paymentstatus.html')

def yourorders(request):
    u=request.user
    o=Order_Details.objects.filter(user=u,payment_status="Completed")
    context={'orders':o}
    return render(request,'yourorders.html',context)





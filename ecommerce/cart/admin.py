from django.contrib import admin
from cart.models import Cart,Payment,Order_Details

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order_Details)
admin.site.register(Payment)


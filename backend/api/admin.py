from django.contrib import admin
from .models import Savings, EqubGroup, EqubMembership, Blog, Transaction

# Register your models here.
admin.site.register(Savings)
admin.site.register(EqubGroup)
admin.site.register(EqubMembership)
admin.site.register(Blog)
admin.site.register(Transaction)
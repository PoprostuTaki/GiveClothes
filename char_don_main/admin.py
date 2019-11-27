from django.contrib import admin

# Register your models here.
from char_don_main.models import Institution, Donation, Category

admin.site.register(Institution)
admin.site.register(Donation)
admin.site.register(Category)

from django.contrib import admin

# Register your models here.
# Register your models here.
# importing models .models is used as model.py and admin.py are in same dir

from .models import Hotel

# django admin is good for cms like stuff
# for More client managed admin a seprate solution needs to be developed
# class PostModelAdmin designs the view of the django admin portal
# admin.ModelAdmin inherits from admin module
# list_display displays the headears for the posts
# search_feild creates a search bar to search content
# list_filter creates filters accrding the items in the parameter
# more info on this link https://docs.djangoproject.com/en/1.9/ref/contrib/admin/

class HotelModelAdmin(admin.ModelAdmin):
	list_display = ["name"]
	search_fields = ["name", "location"]
	list_filter = ["rating", "actual_price"]
	class meta:
		model = Hotel

# this line is to register the posts app to the admin
admin.site.register(Hotel, HotelModelAdmin)
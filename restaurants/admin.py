from django.contrib import admin
from restaurants.models import Restaurant, Food

class RestaurantAdmin(admin.ModelAdmin):
	#fields = ('name', 'phone_number')
	#exclude = ('address',)
	list_display = ('name', 'phone_number', 'address')

class FoodAdmin(admin.ModelAdmin):
	list_filter = ('is_spicy',)

admin.site.register(Restaurant)
admin.site.register(Food)




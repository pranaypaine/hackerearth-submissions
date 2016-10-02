from rest_framework.serializers import ModelSerializer


from hotels.models import Hotel

class HotelSerializer(ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Hotel
		fields = [
			'id',
			'name',
			'image',
			'rating',
			'link',
			'actual_price',
			'discount',
			'location'
		]
		
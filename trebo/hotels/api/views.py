from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

from hotels.models import Hotel

from .serializers import HotelSerializer
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination



class HotelListAPIView(ListAPIView):
	"""docstring for ListAPIView"""
	
	serializer_class = HotelSerializer
	filter_backends = [OrderingFilter]
	pagination_class = PostPageNumberPagination
	def get_queryset(self, *args, **kwrgs):
		queryset = Hotel.objects.all()
		return queryset

class HotelSearchAPIView(ListAPIView):
	"""docstring for ListAPIView"""
	
	serializer_class = HotelSerializer
	def get_queryset(self, *args, **kwrgs):
		#queryset = Hotel.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = Hotel.objects.all()
			queryset = queryset.filter(
			Q(name__icontains=query) |
			Q(location__icontains=query)
			).distinct()
			return queryset
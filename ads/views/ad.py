from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView

from ads.models.ad import Ad
from ads.serializers.ad import AdSerializer, AdImageSerializer, AdUpdateSerializer, AdCreateSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):

        categories = request.GET.getlist('cat', [])

        if categories:
            self.queryset = self.queryset.filter(category__id__in=categories)
        text = request.GET.get("name")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        user_location = request.GET.get('location', None)
        if user_location:
            self.queryset = self.queryset.filter(author__location__name__icontains=user_location)

        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=int(price_from))
        if price_to:
            self.queryset = self.queryset.filter(price__lte=int(price_to))

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    """Display ad by id"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUploadImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer

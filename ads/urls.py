from django.urls import path
from rest_framework import routers

from ads.views.ad import AdListView, AdDetailView, AdUpdateView, AdDeleteView, AdCreateView, AdUploadImageView
from ads.views.category import CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, \
    CategoryCreateView
from ads.views.locations import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    # path('', index),
    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),

    path('ad/', AdListView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/upload_image/', AdUploadImageView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
]

urlpatterns += router.urls

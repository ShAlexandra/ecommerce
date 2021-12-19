from django.urls import include, path
from rest_framework import routers
from .products import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
router.register('image', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

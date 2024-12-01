from . import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import routers



router = routers.DefaultRouter()
router.register('', viewsets.NewsListswagerView, basename='list_news')
router.register('', viewsets.NewsListswagerView, basename='new_news')

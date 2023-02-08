from django.urls import path, include

from app.views import CompositionViewSet, GroupViewSet, ArtistViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('compositions', CompositionViewSet)
router.register('groups', GroupViewSet)
router.register('artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

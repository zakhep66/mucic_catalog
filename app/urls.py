from django.urls import path, include

from app.views import CompositionViewSet, GroupViewSet, ArtistViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('compositions', CompositionViewSet)
get_categories = CompositionViewSet.as_view({'get': 'get_categories'})
router.register('groups', GroupViewSet)
add_composition = GroupViewSet.as_view({'post': 'add_composition'})
router.register('artists', ArtistViewSet)
get_role = ArtistViewSet.as_view({'get': 'get_role'})


urlpatterns = [
    path('', include(router.urls)),
    path('artists/<int:pk>/role/', get_role, name='get_role'),
    path('compositions/<int:pk>/categories/', get_categories, name='get_categories'),
    path('groups/<int:pk>/add-composition/', add_composition, name='add_composition'),
]

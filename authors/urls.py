from rest_framework import routers
from .views import AuthorViewSet

router = routers.DefaultRouter()
router.register('api/authors', AuthorViewSet, 'authors')

urlpatterns = router.urls
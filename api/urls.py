from rest_framework import routers
from .views import ProjectViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register('project', ProjectViewSet)

urlpatterns = router.urls
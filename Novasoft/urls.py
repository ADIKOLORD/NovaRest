from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Novasoft.views import DeveloperAPIViewSet, ContactAPIViewSet

router = DefaultRouter()
router.register('developer', DeveloperAPIViewSet)
router.register('contact', ContactAPIViewSet)


urlpatterns = [
    path('', include(router.urls))
]
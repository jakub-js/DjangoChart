from django.urls import include, path
from rest_framework import routers
from .views import ChartViewSet

router = routers.DefaultRouter()
router.register(r'ChartJS', ChartViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include(r'rest_framework.urls', namespace='rest__framework'))
]

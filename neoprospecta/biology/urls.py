from django.urls import path, include
from rest_framework.routers import DefaultRouter
from neoprospecta.biology import views
from . import views
router = DefaultRouter()

router.register(r'entry', views.EntryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('<int:page>', views.index, name='index')
]

from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from caja import views as cajaViews

router = routers.DefaultRouter()
router.register('caja',cajaViews.AccountBoxViewSet, basename="cajalist")
router.register('detail',cajaViews.DetailBoxViewSet, basename="cajadetail")
router.register('close',cajaViews.CloseBoxViewSet, basename="cajaclose")





urlpatterns = [
    path('', include(router.urls)),
]

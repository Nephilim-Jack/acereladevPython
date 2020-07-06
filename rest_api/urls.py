from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductApiViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('categories', views.CategoryListOnlyApiView.as_view()),
    re_path(r'vendas/(?P<pk>\d+)?', views.OrderApiView.as_view()),
    path('get_token', obtain_auth_token)
]

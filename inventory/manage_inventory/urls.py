from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^fetch/$', views.InventoryActiveList.as_view(), name='fetch'),
    url(r'^add/$', views.InventoryAdd.as_view(), name='add'),
    url(r'^inactive/$', views.InventoryNotActive.as_view(), name='inactive'),
    url(r'^approve/$', views.InventoryApprove.as_view(), name='approve'),
    # url(r'^remove/$', views.DeleteProduct.as_view(), name='remove'),
]


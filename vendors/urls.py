from django.conf.urls import url
from .views import VendorListView, VendorDetailView


urlpatterns = [
    url(r'^$', VendorListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', VendorDetailView.as_view()),
]

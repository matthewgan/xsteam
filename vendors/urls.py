from django.conf.urls import url
from django.views.generic import TemplateView
from .views import VendorListView, VendorDetailView, UploadLogoView, UploadBLView, UploadEPView, UploadRCView,EditInfoView, AddCourseView, UploadCourseView
from . import views


urlpatterns = [
    url(r'^$', VendorListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', VendorDetailView.as_view()),
    url(r'^create/$', views.create_vendor_form, name='create_vendor'),
    url(r'^upLoadLogo/$', UploadLogoView.as_view()),
    url(r'^upLoadBL/$', UploadBLView.as_view()),
    url(r'^upLoadEP/$', UploadEPView.as_view()),
    url(r'^upLoadRC/$', UploadRCView.as_view()),
    url(r'^upLoadCourse/$', UploadCourseView.as_view()),
    url(r'^edit/$', EditInfoView.as_view()),
    url(r'^addCourse/$', AddCourseView.as_view()),
]

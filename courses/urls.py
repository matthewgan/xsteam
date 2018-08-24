from django.conf.urls import url
from .views import CourseListView, CourseDetailView, CourseDetailShowView


urlpatterns = [
    url(r'^$', CourseListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', CourseDetailView.as_view()),
    url(r'^detail/$', CourseDetailShowView.as_view()),
]

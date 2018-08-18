from django.conf.urls import url
from .views import CourseListView, CourseDetailView


urlpatterns = [
    url(r'^$', CourseListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', CourseDetailView.as_view()),
]

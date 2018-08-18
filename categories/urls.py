from django.conf.urls import url
from .views import CategoryListView, CategoryCourseListView


urlpatterns = [
    url(r'^$', CategoryListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', CategoryCourseListView.as_view()),
]
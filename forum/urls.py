from django.conf.urls import url
from .views import ForumView,ForumListView

urlpatterns = [
	url(r'^$', ForumView.as_view(), name='Forum'),
	url(r'^forum$',ForumListView.as_view(),name="forum"),

	]
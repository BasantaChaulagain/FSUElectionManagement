from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^student/$',views.student, name='student'),
	url(r'^viewdata/$',views.viewdata, name='viewdata'),
	url(r'^candidate/$',views.candidate, name='candidate'),
]
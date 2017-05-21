from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Forum

# Create your views here.
class ForumView(CreateView):
	template_name='Forum.html'
	model=Forum
	fields='__all__'


class ForumListView(ListView):
	model=Forum
	template_name='forum.html'

	def get_context_data(self,**kwargs):
		context=super(ForumListView,self).get_context_data(*kwargs)
		context['forum']=Forum.objects.all()
		return context


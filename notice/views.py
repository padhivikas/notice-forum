from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from . models import Notice , Profile

# Create your views here.

# @method_decorator(login_required,name='dispatch')
class NoticeListView(ListView):
	model=Notice
	def get_queryset(self):
		
		if self.request.user.is_superuser:
			return Notice.objects.order_by('-id')
		elif self.request.user.is_authenticated:
			return Notice.objects.filter(Q(branch=None)|Q(branch=self.request.user.profile.branch)).order_by('-id')
		else:
			return Notice.objects.filter(Q(branch=None)).order_by('-id')

@method_decorator(login_required,name='dispatch')
class NoticeDetail(DetailView):
	model=Notice


class ProfileUpdate(UpdateView):
	model=Profile
	fields=["name","branch"]


		

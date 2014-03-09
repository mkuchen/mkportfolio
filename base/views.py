from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.urlresolvers import resolve, reverse
from django import http
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import View

from braces.views import AjaxResponseMixin, JSONResponseMixin
from cloudinary.forms import cl_init_js_callbacks

from base.decorators import require_AJAX
#from referral_center.forms import AdminLinkForm, CreateUserForm, LinkForm, UpdateMemberForm
#from referral_center.models import Member, Referral, ReferralStat
from base.models import Member
from vanilla import CreateView, DetailView, FormView, GenericView, RedirectView, TemplateView, UpdateView

import datetime
import json
import sys
import urllib


class LogoutView(GenericView):
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		logout(request)
		return redirect('/')


@require_AJAX
class LoginAuthView(JSONResponseMixin, AjaxResponseMixin, View):
	content_type = None

	def get_content_type(self):
		return u'application/json'

	@method_decorator(require_POST)
	def post_ajax(self, request, *args, **kwargs):
		user = self.request.user
		if user.is_authenticated():
			#return redirect(request.GET.get('next', '/home/'))
			return self.render_json_response({'status': 'ok', 'next': request.GET.get('next', '/home/'), 'login':'ok'})
		else:
			form = AuthenticationForm(data=request.POST)
			if form.is_valid():
				login(request, form.get_user())
				return self.render_json_response({'status': 'ok', 'next': request.GET.get('next', '/home'), 'login':'ok'})
			else:
				return self.render_json_response({'status': 'ok', 'next': '', 'login':'fail', 'errors':form.errors})

class HomeView(View):
	template_name = 'base/home.html'

	def get(self, request, *args, **kwargs):
		member = Member.objects.get(pk=1)
		context = {
					'member':member,
					'one':'true',
				}
		if request.GET.get('slide', ''):
			context['slide'] = True
		return render(request, self.template_name, context)


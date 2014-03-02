import functools
from models import Member
from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404

from django.utils.decorators import method_decorator

def require_AJAX(view):
    def ajaxOnly(function):
        def wrap(request, *args, **kwargs):
            if not request.is_ajax():
                return HttpResponseForbidden()
            return function(request, *args, **kwargs)
 
        return wrap
 
    view.dispatch = method_decorator(ajaxOnly)(view.dispatch)
    return view

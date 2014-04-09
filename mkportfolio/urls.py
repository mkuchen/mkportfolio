from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

from base.views import HomeView, PortfolioView, LoginAuthView, LogoutView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login-auth/$', LoginAuthView.as_view(), name='auth'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^portfolio/$', PortfolioView.as_view(), name='portfolio'),
    #url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

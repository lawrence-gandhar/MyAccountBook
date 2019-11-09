from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from app.views import dashboard, contacts

# Authorization
urlpatterns = [
    path('', dashboard.index, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'app/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'app/registration/logout.html'), name = 'logout'),
    re_path(r'^accounts/*', RedirectView.as_view(pattern_name='login', permanent=True)),
]

# Dashboard
urlpatterns += [
    path('dashboard/', never_cache(login_required(dashboard.Dashboard.as_view())), name = 'dashboard'),
]

# Contacts
urlpatterns += [
    path('contacts/', never_cache(login_required(contacts.Contacts.as_view())), name = 'contacts'),
    path('contacts/add/', login_required(contacts.add_contacts), name = 'add-contacts'),
    path('contacts/add/<slug:slug>/<int:ins>', login_required(contacts.add_contacts), name = 'add-contacts'),
    
]




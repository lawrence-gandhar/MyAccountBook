from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from app.views import dashboard, contacts, base, invoice, collections

# Authorization
urlpatterns = [
    path('', dashboard.index, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'app/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'app/registration/logout.html'), name = 'logout'),
    re_path(r'^accounts/*', RedirectView.as_view(pattern_name='login', permanent=True)),
    path('unauthorized/', login_required(base.UnAuthorized.as_view()), name = 'unauthorized'),
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
    path('contacts/edit/<slug:slug>/<int:ins>', login_required(contacts.edit_contact), name = 'edit-contact'),
    path('contacts/fetch_extra_edit_forms/', login_required(contacts.fetch_extra_edit_forms), name = 'fetch_extra_edit_forms'),
    path('contacts/delete_contacts/<slug:slug>/<int:ins>/<int:obj>', login_required(contacts.delete_contacts), name = 'delete-contacts'),
    path('contacts/edit_contact_forms/', login_required(contacts.edit_contact_forms), name = 'edit-contact-forms'),
    path('contacts/check_appid/', login_required(contacts.check_app_id), name='check-appid'),
]

# Invoice
urlpatterns += [
    path('invoice/', never_cache(login_required(invoice.Invoice.as_view())), name = 'invoice'),
    path('invoice/create_invoice/', login_required(invoice.create_invoice), name = 'create-invoice'),
    path('invoice/create_invoice/<int:ins>', login_required(invoice.create_invoice), name = 'create-invoice'),
]

# Collections
urlpatterns += [
    path('collections/', never_cache(login_required(collections.Collections.as_view())), name = 'collections'),
    path('collections/<int:ins>', never_cache(login_required(collections.Collections.as_view())), name = 'collections'),
    path('collections/add_collections/', login_required(collections.AddCollections.as_view()), name = 'add-collections'),
]




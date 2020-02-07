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
    path('contacts/', never_cache(login_required(contacts.ContactsView.as_view())), name = 'contacts'),
    path('contacts/add/', never_cache(login_required(contacts.add_contacts)), name = 'add-contacts'),
    path('contacts/add/<slug:slug>/<int:ins>/', never_cache(login_required(contacts.add_contacts)), name = 'add-contacts'),
    path('contacts/edit/<slug:slug>/<int:ins>/', never_cache(login_required(contacts.edit_contact)), name = 'edit-contact'),
    path('contacts/fetch_extra_edit_forms/', never_cache(login_required(contacts.fetch_extra_edit_forms)), name = 'fetch_extra_edit_forms'),
    path('contacts/delete_contacts/<slug:slug>/<int:ins>/<int:obj>/', never_cache(login_required(contacts.delete_contacts)), name = 'delete-contacts'),
    path('contacts/edit_contact_forms/', never_cache(login_required(contacts.edit_contact_forms)), name = 'edit-contact-forms'),
    path('contacts/check_appid/', never_cache(login_required(contacts.check_app_id)), name='check-appid'),
    path('contacts/user_exists_in_list/', never_cache(login_required(contacts.user_exists_in_list)), name='check-appid-user-exist'),
    path('contacts/upload/', never_cache(login_required(contacts.ContactsFileUploadView.as_view())), name='contacts-upload'),
    path('contacts/status_change/<slug:slug>/<int:ins>', never_cache(login_required(contacts.status_change)), name='status-change'),
    path('contacts/delete/<int:ins>', never_cache(login_required(contacts.delete_contact)), name='contacts-delete'),
]

# Invoice
urlpatterns += [
    path('invoice/', never_cache(login_required(invoice.Invoice.as_view())), name = 'invoice'),
    path('invoice/invoice_designer/', never_cache(login_required(invoice.InvoiceDesigner.as_view())), name = 'invoice-designer'),
    path('invoice/invoice_designer/manage/', never_cache(login_required(invoice.manage_invoice_designs)), name = 'manage-invoice-designs'),
    path('invoice/create_invoice/contacts/', never_cache(login_required(invoice.CreateInvoice.as_view())), name = 'create-invoice'),
    path('invoice/create_invoice/contacts/<int:ins>/', never_cache(login_required(invoice.CreateContactInvoice.as_view())), name = 'create-contact-invoice'),
    path('invoice/create_invoice/collections/<int:ins>/', never_cache(login_required(invoice.CreateCollectionInvoice.as_view())), name = 'create-collection-invoice'),
]

# Collections
urlpatterns += [
    path('collections/', never_cache(login_required(collections.view_collections)), name = 'collections'),
    path('collections/contact/<int:ins>/', never_cache(login_required(collections.view_contact_collections)), name = 'contact-collections'),
    path('collections/add_collections/', never_cache(login_required(collections.AddCollections.as_view())), name = 'add-collections'),
    path('collections/add_collections/partial/<int:ins>/', never_cache(login_required(collections.AddPartialCollection.as_view())), name = 'add-partial-collections'),
    path('collections/edit/<int:ins>/', never_cache(login_required(collections.Edit_Collection.as_view())), name = 'edit_collections'),
    path('collections/edit_partial/<int:ins>/<int:obj>/', never_cache(login_required(collections.Edit_PartialCollection.as_view())), name = 'edit_partial_collection'),
]

urlpatterns +=[
    path('invoice/get_pdf/<int:ins>/', never_cache(login_required(invoice.get_pdf)), name = 'get_pdf'),
    
] 

#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()




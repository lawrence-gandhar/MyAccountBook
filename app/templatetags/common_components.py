from django import template

# Django settings from settings.py
from django.conf import settings

# Import models
from app.models import *
from django.contrib.auth.models import User

# Condition operators for models
from django.db.models import Q, When
from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone, safestring

# use Library
register = template.Library()


#*************************************************************************
#   LOADER COMPONENT - MODAL 
#*************************************************************************
@register.simple_tag
def loader_component():
    htm = '''<div class="modal" id="wait_Modal">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">Processing.. Please Wait</h4>
                    </div>
                    <div class="modal-body">                
                        <div class="spinner-grow text-muted"></div>
                        <div class="spinner-grow text-primary"></div>
                        <div class="spinner-grow text-success"></div>
                        <div class="spinner-grow text-info"></div>
                        <div class="spinner-grow text-warning"></div>
                        <div class="spinner-grow text-danger"></div>
                        <div class="spinner-grow text-secondary"></div>
                        <div class="spinner-grow text-dark"></div>
                        <div class="spinner-grow text-light"></div>                
                    </div>
                </div>
            </div>
        </div>'''

    return htm
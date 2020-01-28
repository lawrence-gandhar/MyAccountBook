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
    htm = '''<div class="modal" id="wait_Modal"  tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="background-color: hsla(0, 4%, 26%, 0.87) !important;">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title pull-left">Processing.. Please Wait</h4>
                        <button type="button" onclick="close_modal($(this))" class="close" data-dismiss="modal">&times;</button>
                    </div>
                    <div class="modal-body">                
                        <div id="loader_container" class="loader-custom"></div>
                        <div>
                            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
                                <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" />
                                <path class="checkmark__check" fill="none" d="M16 16 36 36 M36 16 16 36" />
                            </svg>
                        </div> 
                        <div id="modal-text" class="text-center"></div>            
                    </div>
                </div>
            </div>
        </div>'''

    return safestring.mark_safe(htm)
# -*- coding: utf-8 -*-
#
# File: WindowZTool.py
#
# Copyright (c) 2007 by Jean Rodrigo Ferri
# Generator: ArchGenXML 
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Jean Rodrigo Ferri <jeanrodrigoferri@yahoo.com.br>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.windowZ.config import *

# additional imports from tagged value 'import'
from Products.windowZ import permissions


from Products.CMFCore.utils import UniqueObject

    
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='page_width',
        default="100%",
        widget=StringWidget(
            label="Default Page Width",
            size=10,
            description="Width of the iFrame area. This is the default value for the Window content types and may be redefined individually for each Window content. You may use %, px, em, etc.",
            label_msgid="windowZ_tool_label_page_width",
            description_msgid="windowZ_tool_help_page_width",
            i18n_domain='windowZ',
        ),
        required=True
    ),

    StringField(
        name='page_height',
        default="500px",
        widget=StringWidget(
            label="Default Page Height",
            size=10,
            description="Height of the iFrame area. This is the default value for the Window content types and may be redefined individually for each Window content. You may use %, px, em, etc.",
            label_msgid="windowZ_tool_label_page_height",
            description_msgid="windowZ_tool_help_page_height",
            i18n_domain='windowZ',
        ),
        required=True
    ),

    StringField(
        name='base_url',
        default="http://",
        widget=StringWidget(
            label="Base URL",
            description="Base URL provided as prefix for Window relative URLs. It's used only if the option Use Base URL? is checked.",
            label_msgid='windowZ_label_base_url',
            description_msgid='windowZ_help_base_url',
            i18n_domain='windowZ',
        )
    ),

    StringField(
        name='http_proxy',
        widget=StringWidget(
            label="HTTP Proxy",
            description="If there is a proxy in front of the server you should enter the HTTP proxy address. It may seems like http://proxy_address:port or http://username:password@proxy_address:port.",
            label_msgid='windowZ_label_http_proxy',
            description_msgid='windowZ_help_http_proxy',
            i18n_domain='windowZ',
        )
    ),

    BooleanField(
        name='dynamic_window',
        widget=BooleanWidget(
            label="Enable Dynamic Window",
            description="Check this option if you want to use show_window template to show sites provided via URL inside a window.",
            label_msgid='windowZ_label_dynamic_window',
            description_msgid='windowZ_help_dynamic_window',
            i18n_domain='windowZ',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

WindowZTool_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
WindowZTool_schema['title'].required = 0
WindowZTool_schema['title'].widget.visible = {'view':'invisible','edit':'invisible'}
##/code-section after-schema

class WindowZTool(UniqueObject, BaseContent):
    """The windowZ tool. A singleton object that provides functionality
    to Window objects. The fixed id is portal_windowZ.
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(UniqueObject,'__implements__',()),) + (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'windowZ Tool'

    meta_type = 'WindowZTool'
    portal_type = 'WindowZTool'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    content_icon = 'window_icon.gif'
    immediate_view = 'edit'
    default_view = 'edit'
    suppl_views = ()
    typeDescription = "windowZ tool with general settings for Window content types."
    typeDescMsgId = 'description_edit_windowztool'
    toolicon = 'tool.gif'


    actions =  (


       {'action': "string:${object_url}/edit",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': (permissions.ManagePortal,),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = WindowZTool_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    # tool-constructors have no id argument, the id is fixed
    def __init__(self, id=None):
        BaseContent.__init__(self,'portal_windowZ')
        self.setTitle('windowZ Tool')
        
        ##code-section constructor-footer #fill in your manual code here
        ##/code-section constructor-footer


    # tool should not appear in portal_catalog
    def at_post_edit_script(self):
        self.unindexObject()
        
        ##code-section post-edit-method-footer #fill in your manual code here
        ##/code-section post-edit-method-footer


    # Methods

def modify_fti(fti):
    # Hide unnecessary tabs (usability enhancement)
    for a in fti['actions']:
        if a['id'] in ['view', 'metadata', 'sharing']:
            a['visible'] = 0
    return fti

registerType(WindowZTool, PROJECTNAME)
# end of class WindowZTool

##code-section module-footer #fill in your manual code here
##/code-section module-footer




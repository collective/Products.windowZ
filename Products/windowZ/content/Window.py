# -*- coding: utf-8 -*-
#
# File: Window.py
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

import urlparse

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.windowZ.interfaces.IWindow import IWindow
from Products.windowZ.config import *

import zope.interface

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.link import ATLink
from Products.ATContentTypes.content.link import ATLinkSchema
from Products.windowZ import permissions

##code-section module-header #fill in your manual code here
import urllib2
from Products.CMFCore.utils import getToolByName
from Products.windowZ.stripogram import html2text
##/code-section module-header

schema = Schema((

    StringField(
        name='page_width',
        widget=StringWidget(
            label="Page Width",
            description="Enter a value for the page width. If it's not provided the page width will assumes the default value defined in the site setup. You may use %, px, em, etc.",
            size=10,
            label_msgid='windowZ_label_page_width',
            description_msgid='windowZ_help_page_width',
            i18n_domain='windowZ',
        )
    ),

    StringField(
        name='page_height',
        widget=StringWidget(
            label="Page Height",
            description="Enter a value for the page height. If it's not provided the page height will assumes the default value defined in the site setup. You may use %, px, em, etc.",
            size=10,
            label_msgid='windowZ_label_page_height',
            description_msgid='windowZ_help_page_height',
            i18n_domain='windowZ',
        )
    ),

    BooleanField(
        name='hide_metadata',
        default=True,
        widget=BooleanWidget(
            label="Hide Metadata?",
            description="Check this option if you want to hide the page metadata, like title, description, print and send page icons, author, etc.",
            label_msgid='windowZ_label_hide_metadata',
            description_msgid='windowZ_help_hide_metadata',
            i18n_domain='windowZ',
        )
    ),

    BooleanField(
        name='use_base_url',
        widget=BooleanWidget(
            label="Use Base URL?",
            description="Check this option if you want to use the base URL defined in the site setup as a prefix to the provided link.",
            label_msgid='windowZ_label_use_base_url',
            description_msgid='windowZ_help_use_base_url',
            i18n_domain='windowZ',
        )
    ),

    BooleanField(
        name='catalog_page_content',
        default=True,
        widget=BooleanWidget(
            label="Catalog Page Content?",
            description="Check this option if you want to have the content of the provided page indexed in the site catalog and available in the portal search box.",
            label_msgid='windowZ_label_catalog_page_content',
            description_msgid='windowZ_help_catalog_page_content',
            i18n_domain='windowZ',
        )
    ),

    BooleanField(
        name='show_reference',
        widget=BooleanWidget(
            label="Show Reference?",
            description="Check this option if you want to show the provided link as a reference in the bottom of the page.",
            label_msgid='windowZ_label_show_reference',
            description_msgid='windowZ_help_show_reference',
            i18n_domain='windowZ',
        )
    ),

    BooleanField(
        name='inherit_protocol',
        widget=BooleanWidget(
            label="Inherit Protocol?",
            description=("Check this option if you want to inherit the "
                         "URL-protocol for the iframe from the content URL "),
            label_msgid='windowZ_label_inherit_protocol',
            description_msgid='windowZ_help_inherit_protocol',
            i18n_domain='windowZ',
        )
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Window_schema = ATLinkSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
Window_schema['remoteUrl'].accessor = 'getFrameUrl'
##/code-section after-schema

class Window(ATLink):
    """A Window is a content type that shows one URL inside an iFrame
    in a page of the site.
    """
    security = ClassSecurityInfo()
    zope.interface.implements(IWindow)

    # This name appears in the 'add' box
    archetype_name = 'Window'

    meta_type = 'Window'
    portal_type = 'Window'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    content_icon = 'window_icon.gif'
    immediate_view = 'window_view'
    default_view = 'window_view'
    suppl_views = ('window_left_view', 'window_right_view', 'window_both_view')
    typeDescription = "A Window is a content type that shows one URL inside an iFrame in a page of the site."
    typeDescMsgId = 'description_edit_window'


    actions =  (


       {'action': "string:${object_url}",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': (permissions.View,),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/edit",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': (permissions.Modify,),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/properties",
        'category': "object",
        'id': 'metadata',
        'name': 'Properties',
        'permissions': (permissions.Modify,),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': (permissions.ManageProperties,),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = Window_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declareProtected(permissions.View, 'SearchableText')
    def SearchableText(self):
        """Format the title, description and the provided page's content to
        be cataloged by portal_catalog, if user checked
        catalog_page_content option.
        """
        if self.getCatalog_page_content():
            try:
                self.getProxies() # open proxy connection
                remote_url = self.remote_url()
                page = urllib2.urlopen(remote_url)
                page_body = page.read()
            except:
                page_body = ''
            page_content = self._processPageBody(page_body)
        else:
            page_content = ''
        return "%s %s %s" % (self.Title(), self.Description(), page_content)

    # Methods from Interface IWindow

    security.declareProtected(permissions.View, 'getProxies')
    def getProxies(self):
        """Open proxy HTTP connection if it was setting on portal_windowZ tool.
        """
        portal_windowZ = getToolByName(self, 'portal_windowZ')
        http_proxy = portal_windowZ.getHttp_proxy()
        if http_proxy:
            try:
                proxies = {'http': http_proxy}
                proxy_support = urllib2.ProxyHandler(proxies)
                opener = urllib2.build_opener(proxy_support)
                urllib2.install_opener(opener)
            except:
                pass

    security.declareProtected(permissions.View, 'getPageHeight')
    def getPageHeight(self):
        """Returns page_height or the default value from portal_windowZ.
        """
        if self.getPage_height():
            return self.getPage_height()
        else:
            portal_windowZ = getToolByName(self, 'portal_windowZ')
            if portal_windowZ.getPage_height():
                return portal_windowZ.getPage_height()
        return '500px'

    security.declareProtected(permissions.View, 'remote_url')
    def remote_url(self):
        """Returns the Window URL through getFrameUrl method prefixed with
        base_url if it's selected by user.
        """
        if self.getUse_base_url():
            portal_windowZ = getToolByName(self, 'portal_windowZ')
            base_url = portal_windowZ.getBase_url()
            url = "%s%s" % (base_url, self.getFrameUrl())
        else:
            url = self.getFrameUrl()
        if self.getInherit_protocol():
            scheme = urlparse.urlsplit(self.REQUEST.get('SERVER_URL'))[0]
            parts = list(urlparse.urlsplit(url))
            parts[0] = scheme
            url = urlparse.urlunsplit(parts)
        return url

    security.declareProtected(permissions.View, 'getPageWidth')
    def getPageWidth(self):
        """Returns page_width or the default value from portal_windowZ.
        """
        if self.getPage_width():
            return self.getPage_width()
        else:
            portal_windowZ = getToolByName(self, 'portal_windowZ')
            if portal_windowZ.getPage_width():
                return portal_windowZ.getPage_width()
        return '100%'

    # Manually created methods

    security.declarePrivate('_processPageBody')
    def _processPageBody(self, page_body):
        """Process the link body with strip-o-gram library catching only the
        page content.
        """
        ignored_tags = ('img', 'style')
        page_content = html2text(page_body, ignore_tags=ignored_tags)
        return page_content

    def getRemoteUrl(self):
        """Plone 2.5 bug fix."""
        return False



registerType(Window, PROJECTNAME)
# end of class Window

##code-section module-footer #fill in your manual code here
##/code-section module-footer




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
import urllib2

from stripogram import html2text

import zope.interface
from AccessControl import ClassSecurityInfo

from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.link import ATLink
from Products.ATContentTypes.content.link import ATLinkSchema

from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName

from Products.windowZ.interfaces import IWindow
from Products.windowZ.config import PROJECTNAME
from Products.windowZ import WindowZMessageFactory as _

schema = Schema((

    StringField(
        name='page_width',
        widget=StringWidget(
            label=_('windowZ_label_page_width', default="Page Width"),
            description=_('windowZ_help_page_width', default=(
                "Enter a value for the page width. If it's not provided "
                "the page width will assumes the default value defined in "
                "the site setup. You may use %, px, em, etc.")),
            size=10,
        )
    ),

    StringField(
        name='page_height',
        widget=StringWidget(
            label=_('windowZ_label_page_height', default="Page Height"),
            description=_('windowZ_help_page_height', default=(
                "Enter a value for the page height. If it's not provided the "
                "page height will assumes the default value defined in the "
                "site setup. You may use %, px, em, etc.")),
            size=10,
        )
    ),

    BooleanField(
        name='hide_metadata',
        default=True,
        widget=BooleanWidget(
            label=_('windowZ_label_hide_metadata', default="Hide Metadata?"),
            description=_('windowZ_help_hide_metadata', default=(
                "Check this option if you want to hide the page metadata, "
                "like title, description, print and send page icons, author, "
                "etc.")),
        )
    ),

    BooleanField(
        name='use_base_url',
        widget=BooleanWidget(
            label=_('windowZ_label_use_base_url', default="Use Base URL?"),
            description=_('windowZ_help_use_base_url', default=(
                "Check this option if you want to use the base URL defined in "
                "the site setup as a prefix to the provided link.")),
        )
    ),

    BooleanField(
        name='catalog_page_content',
        default=True,
        widget=BooleanWidget(
            label=_('windowZ_label_catalog_page_content',
                    default="Catalog Page Content?"),
            description=_('windowZ_help_catalog_page_content', default=(
                "Check this option if you want to have the content of the "
                "provided page indexed in the site catalog and available "
                "in the portal search box.")),
        )
    ),

    BooleanField(
        name='show_reference',
        widget=BooleanWidget(
            label=_('windowZ_label_show_reference',
                    default="Show Reference?"),
            description=_('windowZ_help_show_reference', default=(
                "Check this option if you want to show the provided link as "
                "a reference in the bottom of the page.")),
        )
    ),

    BooleanField(
        name='inherit_protocol',
        widget=BooleanWidget(
            label=_('windowZ_label_inherit_protocol', "Inherit Protocol?"),
            description=_('windowZ_help_inherit_protocol', default=(
                "Check this option if you want to inherit the "
                "URL-protocol for the iframe from the content URL ")),
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

    meta_type = 'Window'
    _at_rename_after_creation = True

    schema = Window_schema

    security.declareProtected(View, 'SearchableText')
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

    security.declareProtected(View, 'getProxies')
    def getProxies(self):
        """Open proxy HTTP connection if it was setting on portal_windowz tool.
        """
        portal_windowz = getToolByName(self, 'portal_windowz')
        http_proxy = portal_windowz.getHttp_proxy()
        if http_proxy:
            try:
                proxies = {'http': http_proxy}
                proxy_support = urllib2.ProxyHandler(proxies)
                opener = urllib2.build_opener(proxy_support)
                urllib2.install_opener(opener)
            except:
                pass

    security.declareProtected(View, 'getPageHeight')
    def getPageHeight(self):
        """Returns page_height or the default value from portal_windowz.
        """
        if self.getPage_height():
            return self.getPage_height()
        else:
            portal_windowz = getToolByName(self, 'portal_windowz')
            if portal_windowz.getPage_height():
                return portal_windowz.getPage_height()
        return '500px'

    security.declareProtected(View, 'remote_url')
    def remote_url(self):
        """Returns the Window URL through getFrameUrl method prefixed with
        base_url if it's selected by user.
        """
        if self.getUse_base_url():
            portal_windowz = getToolByName(self, 'portal_windowz')
            base_url = portal_windowz.getBase_url()
            url = "%s%s" % (base_url, self.getFrameUrl())
        else:
            url = self.getFrameUrl()
        if self.getInherit_protocol():
            scheme = urlparse.urlsplit(self.REQUEST.get('SERVER_URL'))[0]
            parts = list(urlparse.urlsplit(url))
            parts[0] = scheme
            url = urlparse.urlunsplit(parts)
        return url

    security.declareProtected(View, 'getPageWidth')
    def getPageWidth(self):
        """Returns page_width or the default value from portal_windowz.
        """
        if self.getPage_width():
            return self.getPage_width()
        else:
            portal_windowz = getToolByName(self, 'portal_windowz')
            if portal_windowz.getPage_width():
                return portal_windowz.getPage_width()
        return '100%'

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




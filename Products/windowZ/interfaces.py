# -*- coding: utf-8 -*-
#
# File: interfaces.py
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

import zope.interface
from zope.schema import TextLine, Bool

from Products.windowZ import WindowZMessageFactory as _

class IWindow(zope.interface.Interface):
    """Window interface.
    """

    def remote_url():
        """Returns the Window URL through getFrameUrl method prefixed with
        base_url if it's selected by user.
        """
        pass

    def getPageWidth():
        """Returns page_width or the default value from portal_windowZ.
        """
        pass

    def getPageHeight():
        """Returns page_height or the default value from portal_windowZ.
        """
        pass

    def getProxies():
        """Returns the proxy configuration if it's provided by
        portal_windowZ tool.
        """
        pass

class IWindowZTool(zope.interface.Interface):
    """ Marker for windowZ tool """

class IWindowZControlPanelForm(zope.interface.Interface):
    """WindowZ Control Panel Form"""

class IWindowZSettings(zope.interface.Interface):
    """ Default settings for windowZ content objects """

    page_width = TextLine(
        title=_("windowZ_tool_label_page_width",
                default="Default Page Width"),
        description=_("windowZ_tool_help_page_width", default=(
                "Width of the iFrame area. This is the default value for the "
                "Window content types and may be redefined individually for "
                "each Window content. You may use %, px, em, etc.")),
        required=True,
        default=u"100%")

    page_height = TextLine(
        title=_("windowZ_tool_label_page_height",
                default="Default Page Height"),
        description=_("windowZ_tool_help_page_height", default=(
                "Height of the iFrame area. This is the default value for the "
                "Window content types and may be redefined individually for "
                "each Window content. You may use %, px, em, etc.")),
        required=True)


    base_url = TextLine(
        title=_('windowZ_label_base_url', default="Base URL"),
        description=_('windowZ_help_base_url', default=(
                "Base URL provided as prefix for Window relative URLs. It's "
                "used only if the option Use Base URL? is checked.")),
        default=u"http://")


    http_proxy = TextLine(
        title=_('windowZ_label_http_proxy', default="HTTP Proxy"),
        description=_('windowZ_help_http_proxy', default=(
                "If there is a proxy in front of the server you should enter "
                "the HTTP proxy address. It may seems like "
                "http://proxy_address:port or "
                "http://username:password@proxy_address:port.")),
        )

    dynamic_window = Bool(
        title=_('windowZ_label_dynamic_window',
                default="Enable Dynamic Window"),
        description=_('windowZ_help_dynamic_window', default=(
                "Check this option if you want to use show_window template "
                "to show sites provided via URL inside a window.")),
        )

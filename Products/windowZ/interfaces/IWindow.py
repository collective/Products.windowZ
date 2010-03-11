# -*- coding: utf-8 -*-
#
# File: IWindow.py
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

class IWindow(zope.interface.Interface):
    """Window interface.
    """

    # Methods

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


# end of class IWindow


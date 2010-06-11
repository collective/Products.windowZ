# -*- coding: utf-8 -*-
#
# File: testClasses.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) Window, WindowZTool
#

from Testing import ZopeTestCase
from Products.windowZ.config import *
from Products.windowZ.tests.windowZTestCase import windowZTestCase

# Import the tested classes
from Products.windowZ.content.Window import Window
from Products.windowZ.WindowZTool import WindowZTool

##code-section module-beforeclass #fill in your manual code here
##/code-section module-beforeclass


class testClasses(windowZTestCase):
    """Test-cases for class(es) Window, WindowZTool."""

    ##code-section class-header_testClasses #fill in your manual code here
    ##/code-section class-header_testClasses

    def afterSetUp(self):
        self.folder.invokeFactory('Window', 'window')
        self.window = self.folder['window']

    # from class Window:
    def test_SearchableText(self):
        pass

    # from class Window:
    def test_view(self):
        pass

    # from class Window:
    def test_edit(self):
        pass

    # from class Window:
    def test_metadata(self):
        pass

    # from class Window:
    def test_local_roles(self):
        pass

    # Manually created methods

    def test_iframeurl(self):
        self.window.setRemoteUrl('http://www.plone.org/products')
        self.assertEqual(self.window.getUse_base_url(), False)
        self.assertEqual(self.window.remote_url(),
                         'http://www.plone.org/products')

    def test_iframeurl_with_base(self):
        self.portal.portal_windowZ.setBase_url('ftp://')

        self.window.setRemoteUrl('www.plone.org/products')
        self.window.setUse_base_url(True)
        self.assertEqual(self.window.remote_url(),
                         'ftp://www.plone.org/products')

    def test_iframeurl_inherit_protocol(self):
        self.window.setRemoteUrl('http://www.plone.org/products')
        self.window.setInherit_protocol(True)
        self.assertEqual(self.window.getUse_base_url(), False)
        self.assertEqual(self.window.remote_url(),
                         'http://www.plone.org/products')

    def test_iframeurl_inherit_protocol(self):
        self.window.setRemoteUrl('http://www.plone.org/products')
        self.window.setInherit_protocol(True)
        self.app.REQUEST.set('SERVER_URL', 'https://nohost')
        self.assertEqual(self.window.getUse_base_url(), False)
        self.assertEqual(self.window.remote_url(),
                         'https://www.plone.org/products')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testClasses))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer



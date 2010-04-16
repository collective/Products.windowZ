# -*- coding: utf-8 -*-
#
# File: testSetup.py
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
# Setup tests
#

import os, sys
from Testing import ZopeTestCase
from Products.windowZ.tests.windowZTestCase import windowZTestCase

class testSetup(windowZTestCase):
    """Test cases for the generic setup of the product."""

    ##code-section class-header_testSetup #fill in your manual code here
    ##/code-section class-header_testSetup

    def afterSetUp(self):
        ids = self.portal.objectIds()

    def test_tools(self):
        ids = self.portal.objectIds()
        self.failUnless('portal_windowZ' in ids)

    def test_types(self):
        ids = self.portal.portal_types.objectIds()
        self.failUnless('Window' in ids)

    def test_skins(self):
        ids = self.portal.portal_skins.objectIds()
        self.failUnless('windowZ' in ids)

    def test_workflowChains(self):
        getChain = self.portal.portal_workflow.getChainForPortalType
        self.failUnless('simple_publication_workflow' in getChain('Window'))

    # Manually created methods


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testSetup))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer


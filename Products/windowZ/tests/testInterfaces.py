# -*- coding: utf-8 -*-
#
# File: testInterfaces.py
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

#
# Interface tests
#

import unittest

from zope.interface.verify import verifyClass

from Products.windowZ.content.Window import Window
from Products.windowZ.interfaces import IWindow

class testInterfaces(unittest.TestCase):

    def testInterfacesForWindow(self):
        '''test interface compliance for class Window'''

        self.failUnless(verifyClass(IWindow, Window))

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testInterfaces))
    return suite


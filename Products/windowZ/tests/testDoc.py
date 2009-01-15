# -*- coding: utf-8 -*-
#
# File: testDoc.py
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

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) IWindow, Window
#

from Testing import ZopeTestCase
from Products.windowZ.tests.windowZTestCase import windowZTestCase

# Import the tested classes
from Products.windowZ.interfaces.IWindow import IWindow
from Products.windowZ.content.Window import Window


class testDoc(windowZTestCase):
    """Test-cases for class(es) IWindow, Window."""

    ##code-section class-header_testDoc #fill in your manual code here
    ##/code-section class-header_testDoc

    def afterSetUp(self):
        """
        """
        pass

    # Manually created methods


def test_suite():
    from unittest import TestSuite
    from Testing.ZopeTestCase.zopedoctest import ZopeDocFileSuite

    ##code-section test-suite-in-between #fill in your manual code here
##/code-section test-suite-in-between


    return TestSuite((
        ZopeDocFileSuite('testDoc.txt',
                         package='Products.windowZ.doc',
                         test_class=testDoc),
    ))

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()



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

from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from App.class_init import InitializeClass

from Products.CMFCore.utils import UniqueObject

from Products.windowZ.interfaces import IWindowZSettings

######################################################################
# BBB, instances are removed by an upgrade step in version 2.0
######################################################################

class WindowZTool(UniqueObject, SimpleItem):
    """The windowZ tool. A singleton object that provides functionality
    to Window objects. The fixed id is portal_windowz.
    """

    implements(IWindowZSettings)

    id = 'portal_windowz'
    title = 'windowZ Tool'
    meta_type= 'WindowZTool'
    plone_tool = True
    security = ClassSecurityInfo()

    page_width = FieldProperty(IWindowZSettings['page_width'])
    page_height = FieldProperty(IWindowZSettings['page_height'])
    base_url = FieldProperty(IWindowZSettings['base_url'])
    http_proxy = FieldProperty(IWindowZSettings['http_proxy'])


InitializeClass(WindowZTool)

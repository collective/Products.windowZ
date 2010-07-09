# -*- coding: utf-8 -*-
#
# File: windowZ.py
#
# Copyright (c) 2007 by Jean Rodrigo Ferri
# Generator: ArchGenXML Version 1.5.3 dev/svn
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

from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = "windowZ"

# Permissions
ADD_CONTENT_PERMISSION = 'windowZ: Add Window'
setDefaultRoles(ADD_CONTENT_PERMISSION, ('Manager','Owner'))

product_globals = globals()

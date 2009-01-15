from StringIO import StringIO
from Products.CMFCore.utils import getToolByName

from Products.windowZ.config import RUN_MIGRATIONS
from Products.windowZ.Extensions.Migrations import migrate

def addToListProperty(self, out, propertySheet, property, value):
    """Add the given value to the list in the given property"""
    current = list(propertySheet.getProperty(property))
    if value not in current:
        current.append(value)
        propertySheet.manage_changeProperties(**{property : current})
        print >> out, "Added %s to %s" % (value, property)

def delFromListProperty(self, out, propertySheet, property, value):
    """Delete the given value from the list in the given property"""
    current = list(propertySheet.getProperty(property))
    if value in current:
        current.remove(value)
        propertySheet.manage_changeProperties(**{property : current})
        print >> out, "Deleted %s from %s" % (value, property)

def install(self):
    """Do customized installation"""
    out = StringIO()

    portal_properties = getToolByName(self, 'portal_properties')
    site_properties = getattr(portal_properties, 'site_properties')

    # Set default_page_types
    addToListProperty(self, out, site_properties, 'default_page_types', 'Window')

    # Run Migrations
    if RUN_MIGRATIONS:
        print >> out, migrate(self)

    return out.getvalue()

def uninstall(self):
    """Do customized uninstallation"""
    out = StringIO()

    portal_properties = getToolByName(self, 'portal_properties')
    site_properties = getattr(portal_properties, 'site_properties')

    # Unset default_page_types
    delFromListProperty(self, out, site_properties, 'default_page_types', 'Window')

    return out.getvalue()

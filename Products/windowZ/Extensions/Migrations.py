from StringIO import StringIO
from Products.CMFCore.utils import getToolByName

def reindexWindows(self, out):
    """Reindex all window objects from catalog"""
    catalog = getToolByName(self, 'portal_catalog')
    brains = catalog(meta_type='Window')
    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()
    print >> out, "%s window objects was reindexed" % len(brains)

def migrate(self):
    """Run migrations"""
    out = StringIO()
    print >> out, "Starting windowZ migration"
    reindexWindows(self, out)
    print >> out, "windowZ migrations finished"
    return out.getvalue()

def CMFDisplayPage2windowZ(self):
    """Migrate objects from CMFDisplayPage to windowZ and all configurations"""
    out = StringIO()
    portal = getToolByName(self, 'portal_url').getPortalObject()
    brains = portal.portal_catalog.searchResults(portal_type='DisplayPage')
    portal_windowz = portal.portal_windowZ
    portal_workflow = portal.portal_workflow
    cont = 0

    print >> out, "Migrating windowZ tool"
    page_width = getattr(portal.portal_properties.cmfdisplaypage_properties, 'page_width', '')
    page_height = getattr(portal.portal_properties.cmfdisplaypage_properties, 'page_height', '')
    base_url = getattr(portal.portal_properties.cmfdisplaypage_properties, 'base_url', '')
    portal_windowz.setPage_width(page_width)
    portal_windowz.setPage_height(page_height)
    portal_windowz.setBase_url(base_url)

    print >> out, "Migrating windowZ objects"
    for brain in brains:
        object = brain.getObject()
        parent = object.aq_inner.aq_parent

        id = object.getId()
        title = object.Title()
        description = object.Description()

        remote_url = getattr(object, 'remote_url', '')
        page_width = getattr(object, 'page_width', '')
        page_height = getattr(object, 'page_height', '')
        suppress_left_column = getattr(object, 'suppress_left_column', 0)
        suppress_right_column = getattr(object, 'suppress_right_column', 0)
        hide_metadata = getattr(object, 'hide_metadata', 0)
        use_base_url = getattr(object, 'use_base_url', 0)
        no_iframe = getattr(object, 'no_iframe', 0)

        parent.manage_delObjects(id)

        parent.invokeFactory('Window', id=id, title=title, description=description)
        window = getattr(parent, id)
        window.edit(remote_url=remote_url,
                    page_width=page_width,
                    page_height=page_height,
                    hide_metadata=hide_metadata,
                    use_base_url=use_base_url)

        if suppress_left_column and suppress_right_column:
            window.selectViewTemplate('window_both_view')
        elif suppress_left_column:
            window.selectViewTemplate('window_left_view')
        elif suppress_right_column:
            window.selectViewTemplate('window_right_view')

        #portal_workflow.doActionFor(window, 'publish')

        cont += 1

    print >> out, "%s objects migrated" % cont
    return out.getvalue()

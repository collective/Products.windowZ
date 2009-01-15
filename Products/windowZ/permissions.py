# Permissions used by windowZ

try: # New CMF
    from Products.CMFCore import permissions as CMFCorePermissions
except: # Old CMF
    from Products.CMFCore import CMFCorePermissions

Access           = CMFCorePermissions.AccessContentsInformation
ManagePortal     = CMFCorePermissions.ManagePortal
ManageProperties = CMFCorePermissions.ManageProperties
Modify           = CMFCorePermissions.ModifyPortalContent
View             = CMFCorePermissions.View


from zope.interface import implements

from plone.fieldsets.fieldsets import FormFieldsets
from plone.app.controlpanel.form import ControlPanelForm

from Products.windowZ import WindowZMessageFactory as _
from Products.windowZ.interfaces import IWindowZControlPanelForm
from Products.windowZ.interfaces import IWindowZSettings

class WindowZControlPanelForm(ControlPanelForm):
    """WindowZ Control Panel Form"""

    implements(IWindowZControlPanelForm)

    windowzsettings = FormFieldsets(IWindowZSettings)
    windowzsettings.id = 'windowzsettings'
    windowzsettings.label = _(u'Settings')

    form_fields = FormFieldsets(windowzsettings)

    label = _(u"WindowZ Settings")
    description = _(u"Settings for the WindowZ iFrame contents.")
    form_name = _("WindowZ Settings")

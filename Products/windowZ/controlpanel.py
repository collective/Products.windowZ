from Products.windowZ import WindowZMessageFactory as _
from Products.windowZ.interfaces import IWindowZSettings
from plone.app.registry.browser import controlpanel
from plone.z3cform import layout


class WindowZControlPanelForm(controlpanel.RegistryEditForm):
    """WindowZ Control Panel Form"""

    schema = IWindowZSettings

    label = _(u"WindowZ Settings")
    description = _(u"Settings for the WindowZ iFrame contents.")
    form_name = _("WindowZ Settings")


WindowZControlPanel = layout.wrap_form(
    WindowZControlPanelForm, controlpanel.ControlPanelFormWrapper)

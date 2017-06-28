from plone import api
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


def remove_tool(setup):
    tool = api.portal.get_tool('portal_windowz')
    prefix = IWindowZSettings.__identifier__ + '.'
    for name in IWindowZSettings:
        value = getattr(tool, name, None) or u''
        api.portal.set_registry_record(prefix + name, value)
    portal = api.portal.get()
    del portal['portal_windowz']

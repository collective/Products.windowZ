# -*- coding: utf-8 -*-
from logging import getLogger

from plone import api
from plone.app.upgrade.utils import loadMigrationProfile
from Products.windowZ.interfaces import IWindowZSettings

logger = getLogger('Products.windowZ')


def reinstall_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-Products.windowZ:default'
    )
    logger.info("Products.windowZ generic setup profile re-installed")


def remove_tool(setup):
    setup.runAllImportStepsFromProfile('profile-Products.windowZ:default')
    tool = api.portal.get_tool('portal_windowz')
    prefix = IWindowZSettings.__identifier__ + '.'
    for name in IWindowZSettings:
        value = getattr(tool, name, None) or u''
        api.portal.set_registry_record(prefix + name, value)
    portal = api.portal.get()
    portal.manage_delObjects(['portal_windowz'])

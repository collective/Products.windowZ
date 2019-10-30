=========
Changelog
=========

2.0.1 (2019-10-30)
==================

- Update pt_BR translation
  [ramiroluz]


2.0 (2017-11-07)
================

- Ported to Plone 5: removed WindowZTool and replaced it with registry.
  [tlotze]

- Removed ``show_window`` feature which was apparently unused and didn't work
  as advertised.
  [tlotze]

- Fixed dependencies to ATCT/AT in profiles and test setup
  [MrTango]


1.5 (2013-10-28)
================

- Fixed ``AttributeError: portal_windowZ`` in show_window template,
  even though this template seems unused.  Note that in version 1.3b3
  the id ``portal_windowZ` was renamed to ``portal_windowz`, with a
  lowercase ``z``.  If you get this AttributeError when viewing
  windowz (also with other templates than show_window) then you have
  probably upgraded from an old version and the tool on your website
  still has the old ``portal_windowZ`` id.  In that case you should
  deactivate the windowZ product in the Add-ons control panel and
  activate it again.
  [maurits]

1.4.1 (2012-11-30)
==================

* Fixed views with special column handling
  [tom_gross]

1.4 - 2012-09-09
================

* enhanced error catching in SearchableText-method
  [tom_gross]
* prevent redirection to external link in navtree
  [petschki]

1.3 - 2012-03-30
================

* remove workaround for Plone 2.5 which breaks with c.flowplayer
  in Plone 4.2b1 [tom_gross]
* moved code to github.com.
  [tom_gross, malthe]

1.3b3 - 2011-07-17
==================

* minor cleanup, object_title was being used inconsistently  [auspex]

* make it work in Plone 4 [ yurj, jensens]

1.3-beta2 - 2010-07-27
======================

* moved z2-Interface to z3-interface
* fixed `window_view` to work with Plone 4.0
* added inherit_protocol flag, which allows to inherit the protocol schema
* use '_' to mark messagestrings in code
* use GenericSetup-profile for installing product
* factored out stripogram. it is an egg dependency now.
* The WindowZTool is no content any longer
* Added form-enabled configlet
* changed compatibility to Plone 3 and 4
* added German translations.

[tom_gross]

1.3-beta
========

* Eggified product

1.2.1 - 2008-06-03
==================

* Added Danish translations.
  [jacobv]

1.2 - 2007-08-21
================

* Added show_window template to show external sites inside portal just
  providing the site URL as a value for the url variable.
  [ferri]

* Added tests from default ArchGenXML support.
  [ferri]

* Moved document_byline macro at view template.
  [ferri]

* Plone 3.0 compatibility.
  [ferri]

* Regenerated with the last ArchGenXML from 1.5 branch.
  [ferri]

* Added French translations.
  [landure]

* Included stripogram as an embeded library in windowZ. Now it's not a
  dependencie anymore.
  [ferri]

1.1 - 2006-09-12
================

* Provided migration script to migrate objects and configurations from
  CMFDisplayPage to windowZ.
  [ferri]

* Updated all translations.
  [ferri]

* Added proxy support for content catalogation when Zope instances are running
  behind a proxy server.
  [ferri]

* Added Italian translations.
  [befree]

* Removing workflow for portal_windowZ tool.
  [ferri]

* Fixed bug in Install.py when trying to remove portal_windowZ from
  idsNotToList property.
  [ferri]

* Removing portal_windowZ tool from portal search with the types_not_searched
  property.
  [ferri]

* Added AppInstall.py which add Window to default_page_types property. It
  enables users to select a Window as the default page of a folder.
  [ferri]

* Implemented feature directly in ArchGenXML to automatically uncatalog
  portal_windowZ tool.
  [ferri]

* Generalized path for generation scripts and i18ndude.
  [ferri]

* Added the link address inside iFrame because some browsers doesn't have
  iFrame support.
  [ferri]

1.0.1 - 2006-08-09
==================

* Criated migration function to reindex all window objects to remove from
  catalog the getRemoteUrl method.
  [ferri]

* Invaliding method getRemoteUrl to fix a Plone 2.1.3 and 2.5 introduced bug.
  [ferri]

* Added Spanish translations.
  [thegoldenaura]

* Added Portuguese translations.
  [thegoldenaura]

1.0 - 2006-03-15
================

* First public release.
  [ferri]

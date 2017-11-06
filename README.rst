================
Products.windowZ
================

.. contents:: Table of Contents

.. image:: https://secure.travis-ci.org/collective/Products.windowZ.png?branch=master
    :target: http://travis-ci.org/collective/Products.windowZ

.. image:: https://coveralls.io/repos/collective/Products.windowZ/badge.png?branch=master
    :target: https://coveralls.io/r/collective/Products.windowZ

Many people would like to have external web pages inside your Plone site.
windowZ was born to do it, in an elegant way.

windowZ provides a new content type, named Window, that is similar to the
content type Link. It shows the provided relative or absolute URL inside an
iFrame rendered as a Plone page.

However we can configure windowZ to do some usefull things to us, like:

* Displays inside Plone any outside-to-Plone web page available on the web.
* Catalogs the content from the provided web pages. Users may choose which
  pages to catalog.
* Gives users the ability to hide left, right or both columns of the Plone
  site.
* Each page may be individually resized.
* Users may opt display the content metadata or show only the web page
  without any meta-information in the Plone.

windowZ was the CMFDisplayPage product available only in the Plone collective
repository without any release. But it was too hard to mantain and evolute it
because its code was pure CMF-aware.

So it was rewrited from scratch using ArchGenXML to generate the code. Just
in a few hours of work. Now we can finally make a release! ArchGenXML rocks!

It's pronunciation may be: windows, windoze, window(Z) of Zope... You are free
to choose the way... ;-)

Please, help us to improve and translate windowZ!

**Please note: version 2.x only work on Plone 5.0.x and higher, for Plone 4 use 1.x.**

collective.localstyles
======================

With this Plone Addon you can add local styles within a subsection of your
Plone site.

After installation you can upload a css file, named ``local.css`` anywhere to a
folderish content item. This css file is then included for this folder and all
content items below. ``ISite`` based objects like ``collective.lineage`` based
subsites below a folder with a ``local.css`` file won't use it.

This product registers a viewlet named ``collective.localstyles.viewlet``,
which is included in ``plone.app.layout.viewlets.interfaces.IHtmlHead`` and is
responsible for injecting the ``local.css`` file.

This product is inspired by this discussion:
http://plone.293351.n2.nabble.com/CSS-for-a-single-page-td7559936.html

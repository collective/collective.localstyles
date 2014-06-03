collective.localstyles
======================

With this Plone Addon you can add local styles within a subsection of your
Plone site.

After installation you can upload a css file, named ``localstyles.css``
anywhere to a folderish content item. This css file is then included for this
folder and all content items below. The traversing stops for ``ISite`` based
objects, which a ``localstyles.css`` file within a ``ISite`` (e.g. a
``collective.lineage`` site) isn't used for folders, which are in higher
hierachy of the content tree.

This product registers a viewlet named ``collective.localstyles.viewlet``,
which is included in ``plone.app.layout.viewlets.interfaces.IHtmlHead`` and is
responsible for injecting the ``localstyles.css`` file.

This product is inspired by this discussion:
http://plone.293351.n2.nabble.com/CSS-for-a-single-page-td7559936.html

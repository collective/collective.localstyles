from Acquisition import aq_parent
from plone.app.layout.viewlets.common import ViewletBase
from zope.component.interfaces import ISite
from plone.folder.interfaces import IFolder

LOCALSTYLES_FILES = ['localstyles.css', 'localstyles_css']


class StyleIncluderViewlet(ViewletBase):

    @property
    def localstyles_url(self):
        context = self.context

        def _get_localstyles(context):
            if IFolder.providedBy(context):
                for it in LOCALSTYLES_FILES:
                    if it in context:
                        return context[it]

            if ISite.providedBy(context):
                # Stop traversing at ISite boundaries
                return None

            else:
                # Try to get localstyles file from parent
                return _get_localstyles(aq_parent(context))

        localstyles = _get_localstyles(context)
        return localstyles.absolute_url() if localstyles else None

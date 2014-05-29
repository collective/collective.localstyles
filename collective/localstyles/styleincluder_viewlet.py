from Acquisition import aq_parent
from plone.app.layout.viewlets.common import ViewletBase
from zope.component.interfaces import ISite
from plone.folder.interfaces import IFolder

LOCALSTYLES_FILE = 'localstyles.css'


class StyleIncluderViewlet(ViewletBase):

    @property
    def localstyles_url(self):
        context = self.context

        def _get_localstyles(context):
            if IFolder.providedBy(context) and LOCALSTYLES_FILE in context:
                return context[LOCALSTYLES_FILE]

            elif ISite.providedBy(context):
                # Stop traversing at ISite boundaries
                return None

            else:
                # Try to get localstyles file from parent
                return _get_localstyles(aq_parent(context))

        localstyles = _get_localstyles(context)
        return localstyles.absolute_url() if localstyles else None

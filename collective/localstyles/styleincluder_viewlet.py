from Acquisition import aq_parent
from plone.app.layout.viewlets.common import ViewletBase
from zope.component.interfaces import ISite


LOCALSTYLES_FILE = 'localstyles.css'


class StyleIncluderViewlet(ViewletBase):

    @property
    def localstyle_file(self):
        context = self.context

        def _get_localstyles(context):
            if LOCALSTYLES_FILE in context:
                return context[LOCALSTYLES_FILE]

            elif ISite.providedBy(context):
                # Stop traversing at ISite boundaries
                return None

            else:
                # Try to get localstyles file from parent
                return _get_localstyles(aq_parent(context))

        return _get_localstyles(context)

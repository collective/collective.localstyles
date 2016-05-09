from plone.app.layout.viewlets.common import ViewletBase

LOCALSTYLES_FILES = ['localstyles.css', 'localstyles_css']


class StyleIncluderViewlet(ViewletBase):

    @property
    def localstyles_url(self):
        context = self.context

        for it in LOCALSTYLES_FILES:
            style_file = context.get(it, None)
            if style_file:
                return style_file.absolute_url()

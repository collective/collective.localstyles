from setuptools import setup
from setuptools import find_packages

version = '1.1'

long_desc = '{}\n{}'.format(
    open("README.rst").read(),
    open("CHANGES.rst").read(),
)

setup(
    name='collective.localstyles',
    version=version,
    description="Add local styles to subsections in your Plone site.",
    long_description=long_desc,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone collective theme style',
    author='Johannes Raggam',
    author_email='office@programmatic.pro',
    url='https://github.com/collective/collective.localstyles',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
        'zope.publisher',
        'plone.browserlayer',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing [robot]',
            'unittest2',
        ]
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """)

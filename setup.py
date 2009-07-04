from distutils.core import setup

setup(
    name='pinax-syncr-delicious',
    version=__import__('delicious').__version__,
    description='An app for syncronizing del.icio.us bookmarks in Pinax. Based on http://code.google.com/p/django-syncr/.',
    author='DoUYourself',
    author_email='duy@rhizomatik.net',
    url='http://github.com/duy/pinax-syncr-delicious/',
    packages=[
        'delicious',
    ],
    package_dir={'delicious': 'delicious'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)

from setuptools import setup


setup(
    # So apparently distutils sdist grabs the python package matching the package name.
    # In order to install nothign, I have to mangle the package name...
    name='mangle.asottile.yaml',
    description="asottile's extensions to pyyaml.",
    url='http://github.com/asottile/asottile.yaml',
    version='0.1.0',

    author='Anthony Sottile',
    author_email='asottile@umich.edu',

    platforms='all',
    classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    # we install nothing at all, just to prove a point.
    # packages=['asottile.yaml'],
    # namespace_packages=['asottile'],
    install_requires=[
        'pyyaml',
    ],
)

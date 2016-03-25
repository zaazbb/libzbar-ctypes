from distutils.core import setup
import libzbar
setup(
    name='libzbar',
    description='Python ctypes libzbar wrapper',
    provides=['zbar'],
    requires=[],
    long_description=
    """
    This package is a python ctypes wrapper for the libzbar api 
    """,
    version=libzbar.version,
    packages=['libzbar'],
    package_dir={'libzbar': './libzbar'},
    url='https://github.com/zaazbb/zbar_ctypes',
    author='zaazbb',
    author_email='zaazbb@163.com',
    platforms='Linux',
    license='GNU Library or Lesser General Public License (LGPL)'
)

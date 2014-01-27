try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name            = 'moshy',
    version         = '0.1',
    author          = 'Kevin Roy',
    author_email    = 'kiniou@gmail.com',
    packages        = [
    ],
    scripts         = [
        'moshy'
    ],
    license         = "GPLv3",
    description     = "Mosh with profile",
)

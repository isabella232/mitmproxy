from setuptools import setup, find_packages
from codecs import open
import os

from mitmproxy import version

# Based on https://github.com/pypa/sampleproject/blob/master/setup.py
# and https://python-packaging-user-guide.readthedocs.org/

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mitmproxy",
    version=version.VERSION,
    description="An interactive, SSL-capable, man-in-the-middle HTTP proxy for penetration testers and software developers.",
    long_description=long_description,
    url="http://mitmproxy.org",
    author="Aldo Cortesi",
    author_email="aldo@corte.si",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Security",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Software Development :: Testing"
    ],
    packages=find_packages(include=[
        "mitmproxy", "mitmproxy.*",
        "pathod", "pathod.*",
    ]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "mitmproxy = mitmproxy.tools.main:mitmproxy",
            "mitmdump = mitmproxy.tools.main:mitmdump",
            "mitmweb = mitmproxy.tools.main:mitmweb",
            "pathod = pathod.pathod_cmdline:go_pathod",
            "pathoc = pathod.pathoc_cmdline:go_pathoc"
        ]
    },
    # https://packaging.python.org/en/latest/requirements/#install-requires
    # It is not considered best practice to use install_requires to pin dependencies to specific versions.
    install_requires=[
        "backports.ssl_match_hostname>=3.5.0.1, <3.6",
        "blinker>=1.4, <1.5",
        "click>=6.2, <7.0",
        "certifi>=2015.11.20.1",  # no semver here - this should always be on the last release!
        "configargparse>=0.10, <0.12",
        "construct>=2.5.2, <2.6",
        "cryptography>=1.3, <1.6",
        "cssutils>=1.0.1, <1.1",
        "Flask>=0.10.1, <0.12",
        "h2>=2.5.0, <3",
        "html2text>=2016.1.8, <=2016.9.19",
        "hyperframe>=4.0.1, <5",
        "jsbeautifier>=1.6.3, <1.7",
        "lxml>=3.5.0, <=3.6.0",  # no wheels for 3.6.1 yet.
        "Pillow>=3.2, <3.5",
        "passlib>=1.6.5, <1.7",
        "pyasn1>=0.1.9, <0.2",
        "pyOpenSSL>=16.0, <17.0",
        "pyparsing>=2.1.3, <2.2",
        "pyperclip>=1.5.22, <1.6",
        "requests>=2.9.1, <2.12",
        "tornado>=4.3, <4.5",
        "urwid>=1.3.1, <1.4",
        "watchdog>=0.8.3, <0.9",
        "brotlipy>=0.5.1, <0.7",
    ],
    extras_require={
        ':sys_platform == "win32"': [
            "pydivert>=0.0.7, <2.0",
        ],
        ':sys_platform != "win32"': [
        ],
        'dev': [
            "flake8>=2.6.2, <3.1",
            "mypy-lang>=0.4.5, <4.6",
            "rstcheck>=2.2, <3.0",
            "tox>=2.3, <3",
            "mock>=2.0, <2.1",
            "pytest>=3, <3.1",
            "pytest-cov>=2.2.1, <3",
            "pytest-timeout>=1.0.0, <2",
            "pytest-xdist>=1.14, <2",
            "pytest-faulthandler>=1.3.0, <2",
            "sphinx>=1.3.5, <1.5",
            "sphinx-autobuild>=0.5.2, <0.7",
            "sphinxcontrib-documentedlist>=0.4.0, <0.5",
            "sphinx_rtd_theme>=0.1.9, <0.2",
        ],
        'contentviews': [
            "protobuf>=3.1.0, <3.2",
            # TODO: Find Python 3 replacement
            # "pyamf>=0.8.0, <0.9",
        ],
        'examples': [
            "beautifulsoup4>=4.4.1, <4.6",
            "pytz>=2015.07.0, <=2016.7",
        ]
    }
)

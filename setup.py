# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="CUBO_LOCKTON",
    version="1.0",
    description="cubo inteligente comprometidos con la Seguridad y la Salud",
    author="V.J.R",
    author_email="email del autor",
    url="url del proyecto",
    license="tipo de licencia",
    scripts=["cuboficial.py"],
    console=["cuboficial.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)
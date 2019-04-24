from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

import eigency


extensions = [
    Extension("fastronWrapper.fastronWrapper", ["fastronWrapper/fastronWrapper.pyx"],
        include_dirs = [".", "fastronWrapper"] + eigency.get_includes()
    ),
]

dist = setup(
    #name = "fastronWrapper",
    #version = "1.0",
    ext_modules = cythonize(extensions),
    #packages = ["fastronWrapper"]
)

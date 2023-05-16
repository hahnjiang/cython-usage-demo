from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "demo",
        sources=["cpyx/demo.pyx"],
        libraries=["m"]  # Unix-like specific
    )
]

setup(
    name='Hello world app',
    # ext_modules=cythonize(ext_modules),
    ext_modules=cythonize("cpyx/calc.pyx"),
    zip_safe=False,
)

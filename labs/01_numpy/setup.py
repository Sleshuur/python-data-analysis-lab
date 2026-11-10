from pathlib import Path
from setuptools import setup, Extension
from Cython.Build import cythonize

# Запуск: python setup.py build_ext --inplace
source = Path(__file__).with_name("sum_squares.pyx")
setup(
    name="numpy-lab-cython",
    ext_modules=cythonize(
        [Extension("sum_squares", [str(source)])],
        compiler_directives={"language_level": "3"},
    ),
)

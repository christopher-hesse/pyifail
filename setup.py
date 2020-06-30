from setuptools import setup, find_packages

setup_dict = dict(
    name="pyifail",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
    ],
    extras_require={
    },
    python_requires=">=3.7.0",
)

setup(**setup_dict)

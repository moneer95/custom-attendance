from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_attendance/__init__.py
from custom_attendance import __version__ as version

setup(
	name="custom_attendance",
	version=version,
	description="a",
	author="a",
	author_email="a",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

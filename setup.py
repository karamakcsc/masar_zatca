from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in masar_zatca/__init__.py
from masar_zatca import __version__ as version

setup(
	name="masar_zatca",
	version=version,
	description="Masar Zatca",
	author="KCSC",
	author_email="info@kcsc@1978",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

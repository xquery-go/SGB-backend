
import re
from setuptools import setup, find_packages

with open('core/__init__.py', 'rb') as module:
    current_version = str(eval(re.search(r'CORE_VERSION\s+=\s+(.*)',
                          module.read().decode('utf-8')).group(1)))

# Write code to update core version


setup(
    name='CORE',
    version=current_version,
    description='Core modules for project',
    author='Abhilash',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.10",
    zip_safe=False,
)

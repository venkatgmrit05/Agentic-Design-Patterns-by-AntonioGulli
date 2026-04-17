# setup.py placed at root directory
from setuptools import setup, find_packages
# import re

# __version__ = re.findall(
#     r""" __version__ =["']+([0-9\.\-dev]*)["']+""",
#     open('linkedinjobautomation/__init__.py').read(),
# )[0]

prod_requirements = []
dev_requirements = []

setup(
    name='agentic',
    version='1.1.0',
    author='umavenkatkaranam',
    description='agentic analytics',
    long_description='agentic workflow',
    url='',
    keywords='agentic, python ,analytics, setuptools',
    # packages='find:',
    packages=find_packages(),
    python_requires='>=3.7, <4',
    install_requires=['pandas', 'numpy', 'Scrapy',
                      'beautifulsoup4', 'pandas', 'seaborn', 'matplotlib',
                      'openpyxl'],
    extras_require={
        'test': ['pytest', 'coverage'],
    },
    package_data={
        'agentic': [],
    },
    entry_points={
        'console_scripts': [
            'agentic=agentic:autoapply',
        ]
    }
)

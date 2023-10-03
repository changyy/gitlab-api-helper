from setuptools import setup, find_packages
import os
import re
import pathlib

CWD = pathlib.Path(__file__).parent.resolve()

VERSION = '1.0.0' 
with open(os.path.join(CWD, 'gitlab_api_helper', '__init__.py'), 'r') as f:
    re_version_pattern = re.compile(r"=[\s]*['\"]([0-9\.]+)['\"]")
    for line in f:
        line = line.strip()
        if line.find('version') >= 0:
            extractVersionInfo = re_version_pattern.search(line)
            if extractVersionInfo:
                VERSION = extractVersionInfo.group(1)

PYTHON_REQUIRES = ">=3.10"
URL = "https://github.com/changyy/gitlab-api-helper"
DOWNLOAD_URL = "https://pypi.org/project/gitlab-api-helper/"
DESCRIPTION = 'A simple tool that calls gitlab api to generate the repo summary'
LONG_DESCRIPTION = DESCRIPTION
LONG_DESCRIPTION_TYPE = 'text/plain'
try:
    with open(os.path.join(CWD, "README.md"), 'r') as f:
        data = f.read()
        if len(data) > 10:
            LONG_DESCRIPTION = data
            LONG_DESCRIPTION_TYPE = 'text/markdown'
except Exception as e:
    pass


INSTALL_REQUIRES = ['pandas']
try:
    with open(os.path.join(CWD, "requirements.txt"), 'r') as f:
        INSTALL_REQUIRES = [s.strip() for s in f.read().split("\n")]
except Exception as e:
    pass

setup(
    name="gitlab-api-helper", 
    version=VERSION,
    author="Yuan-Yi Chang",
    author_email="<changyy.csie@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_TYPE,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    keywords=['python', 'gitlab', 'api', 'report', 'summary'],
    python_requires=PYTHON_REQUIRES,
    url=URL,
    download_url=DOWNLOAD_URL,
    entry_points={
        'console_scripts': [
            'gitlab-api-helper = gitlab_api_helper.cmd:main',
        ],
    },
    classifiers= [
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)

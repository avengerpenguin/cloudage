from typing import Any, Mapping, Optional, Sequence, Union

import setuptools
from setuptools.dist import Distribution
from setuptools.extension import Extension

class Command: ...

def setup(
    *,
    name: Optional[str] = ...,
    version: Optional[str] = ...,
    description: Optional[str] = ...,
    long_description: Optional[str] = ...,
    long_description_content_type: Optional[str] = ...,
    author: Optional[str] = ...,
    author_email: Optional[str] = ...,
    maintainer: Optional[str] = ...,
    maintainer_email: Optional[str] = ...,
    url: Optional[str] = ...,
    download_url: Optional[str] = ...,
    packages: Optional[Sequence[str]] = ...,
    py_modules: Optional[Sequence[str]] = ...,
    scripts: Optional[Sequence[str]] = ...,
    ext_package: Optional[str] = ...,
    ext_modules: Optional[Sequence[Extension]] = ...,
    classifiers: Optional[Sequence[str]] = ...,
    distclass: Optional[Distribution] = ...,
    script_name: Optional[str] = ...,
    script_args: Optional[Sequence[str]] = ...,
    options: Optional[Mapping[str, str]] = ...,
    license: Optional[str] = ...,
    keywords: Optional[Union[Sequence[str], str]] = ...,
    platforms: Optional[Union[Sequence[str], str]] = ...,
    cmdclass: Optional[Mapping[str, Command]] = ...,
    package_dir: Optional[Mapping[str, str]] = ...,
    include_package_data: Optional[bool] = ...,
    package_data: Optional[Mapping[str, str]] = ...,
    zip_safe: Optional[bool] = ...,
    install_requires: Optional[Union[Sequence[str], str]] = ...,
    entry_points: Optional[Mapping[str, Union[str, Sequence[str]]]] = ...,
    extras_require: Optional[Mapping[str, Union[str, Sequence[str]]]] = ...,
    python_requires: Optional[str] = ...,
    namespace_packages: Optional[Sequence[str]] = ...,
    eager_resources: Optional[Sequence[str]] = ...,
    project_urls: Optional[Mapping[str, str]] = ...,
    **kwargs: Any,
) -> Distribution: ...

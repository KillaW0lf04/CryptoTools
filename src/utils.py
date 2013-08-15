__author__ = 'Michael Aquilina'

import pkg_resources
from distutils.version import StrictVersion


def is_package_installed(package_name, min_required_version=None):
    try:
        package_version = pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        installed = False
    else:
        if min_required_version is None:
            min_required_version = '0.0'

        installed = StrictVersion(package_version) >= StrictVersion(min_required_version)

    return installed
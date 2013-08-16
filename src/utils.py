__author__ = 'Michael Aquilina'

import math
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


def zip2(text1, text2):
    large_text = text1 if len(text1) > len(text2) else text2
    small_text = text2 if len(text2) < len(text1) else text1

    # Expand the small text
    mul_value = int((math.ceil(len(large_text) / float(len(small_text)))))
    small_text = small_text * mul_value

    return zip(small_text, large_text)

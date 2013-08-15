from src.utils import is_package_installed


def test_is_package_installed():
    assert not is_package_installed('ThisPackageDoesNotExist')
    assert is_package_installed('PyCrypto', '2.6')
    assert is_package_installed('PyCrypto')

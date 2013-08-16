from src.utils import is_package_installed, zip2


def test_is_package_installed():
    assert not is_package_installed('ThisPackageDoesNotExist')
    assert is_package_installed('PyCrypto', '2.6')
    assert is_package_installed('PyCrypto')


def test_zip2():
    text1 = 'hello'
    text2 = 'hello world'

    # Resultant length should be the length of the largest text
    assert len(zip2(text1, text2)) == len(text2)
    assert len(zip2(text2, text1)) == len(text2)

    result = zip2(text1, text2)

    assert ''.join([c1 for c1, _ in result]) == 'hellohelloh'
    assert ''.join([c2 for _, c2 in result]) == 'hello world'

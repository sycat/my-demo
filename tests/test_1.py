import pytest


def test_1_1(page):
    page.goto("https://www.google.com")
    assert True

@pytest.mark.facebook
def test_1_2(page):
    page.goto("https://www.facebook.com")
    assert True

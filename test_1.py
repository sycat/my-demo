import time
from playwright.sync_api import Page, expect


def test_1_1(page: Page):
    page.goto('https://www.google.com/')

def test_1_2(page: Page):
    page.goto('https://www.github.com/')
    assert False

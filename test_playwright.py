import time
from playwright.sync_api import Page, expect


def test_playwright_1(page: Page):
    page.goto('https://www.google.com/')
    time.sleep(3)
    assert True

def test_playwright_2(page: Page):
    page.goto('https://www.instagram.com/')
    time.sleep(3)
    assert False

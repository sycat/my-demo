from playwright.sync_api import Page
import time


def test_1_1(page: Page):
    page.goto('https://www.facebook.com/')
    time.sleep(5)
    page.screenshot(path='outputs/screenshot.png')

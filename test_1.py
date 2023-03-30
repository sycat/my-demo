import time
from playwright.sync_api import Page, expect


def test_1_1(page: Page):
    page.goto('https://www.facebook.com')
    expect(page.get_by_test_id("royal_email")).to_be_visible()

def test_1_2(page: Page):
    page.goto('https://www.facebook.com', wait_until='load')
    expect(page.get_by_test_id("royal_email")).to_be_visible()

def test_1_3(page: Page):
    page.goto('https://www.facebook.com', wait_until='domcontentloaded')
    expect(page.get_by_test_id("royal_email")).to_be_visible()

def test_1_4(page: Page):
    page.goto('https://www.facebook.com', wait_until='networkidle')
    expect(page.get_by_test_id("royal_email")).to_be_visible()

def test_1_5(page: Page):
    page.goto('https://www.facebook.com', wait_until='commit')
    page.screenshot(path='outputs/test_1_5_1.png')
    time.sleep(5)
    page.screenshot(path='outputs/test_1_5_2.png')
    expect(page.get_by_test_id("royal_email")).to_be_visible()

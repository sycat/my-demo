import re
import pytest
from playwright.sync_api import Page, expect


def test_home(page):
    page.goto('https://stg.idprotect.trendmicro.com/ja')
    with page.context.expect_page() as new_page_info:
        page.locator("div").filter(has_text=re.compile(r"^個人情報盗難のリスクを評価$")).first.click(timeout=15000)
    new_page = new_page_info.value
    expect(new_page).to_have_url(re.compile(r'https://helpcenter\.trendmicro\.com/ja-jp/dwa/idp/assessment/.*'), timeout=20000)

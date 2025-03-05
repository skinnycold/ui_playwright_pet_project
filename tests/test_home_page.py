from time import sleep

from pages.home_page import HomePage
import pytest
from data.home_page_data import data_navigation


def test_home_page(page):
    home_page = HomePage(page)
    home_page.open()
    home_page.check_title('Home Page')
    home_page.check_h1('Home Page')

@pytest.mark.parametrize('page_method, title , h1_title', data_navigation)
def test_navigation(page, page_method, title, h1_title):
    home_page = HomePage(page)
    home_page.open()
    home_page.agree_cookie()
    getattr(home_page, page_method)()
    home_page.check_title(title)
    home_page.check_h1(h1_title)


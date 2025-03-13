import pytest
from data.home_page_data import data_navigation

@pytest.mark.regression
@pytest.mark.parametrize('page_method, title , h1_title', data_navigation)
def test_navigation(home_page, page_method, title, h1_title):
    """
    Проверяет навигацию по страницам приложения
    """
    home_page.open()
    home_page.agree_cookie()
    getattr(home_page, page_method)()
    home_page.check_title(title)
    home_page.check_h1(h1_title)


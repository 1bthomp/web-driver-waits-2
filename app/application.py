from page.base_page import Page
from page.cart_page import CartPage
from page.header import Header
from page.main_page import MainPage
from page.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultsPage(driver)



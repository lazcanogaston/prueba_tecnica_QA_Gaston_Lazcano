from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        print("ENTRA")
        super().__init__(driver)

    #Locators:
    topBarNavCategoriesList = '//ul[@id="menu-header-es-1"]/li[contains(@class,"nav-item-level-0")]/a/span'
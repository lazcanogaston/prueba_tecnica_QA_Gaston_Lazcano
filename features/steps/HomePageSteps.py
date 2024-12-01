from collections import Counter
import time
from behave import given, when, then
from pages.HomePage import HomePage
import data_prod
from unidecode import unidecode

#logger = logging.getLogger("LOG_Alten")

@given('I am in the home page')
def navigateToHomePage(context):
    
    context.home_page = HomePage(context.driver)
    context.home_page.get_page(data_prod.prodUrl)
    context.logger.info(data_prod.prodUrl + "page loaded successfully.")

@then('The top navigation bar contains all the expected categories')
def verifyNavigationTopBarCategoryNames(context):
    #get from the input data set all the expected main categories
    expected_categories = [data["categoryName"] for data in data_prod.topNavigationBar.values()]
    context.logger.info(f"Expected categories in home page: {expected_categories}")
    #get from page the present categories
    time.sleep(5)
    element_categories_list = context.home_page.find_elements(context.home_page.topBarNavCategoriesList)
    #unicode is used to remove the accent mark
    categoryNames = list(map(lambda a: unidecode(a.text) ,element_categories_list))    
    context.logger.info(f"Current categories in home page: {categoryNames}")
    time.sleep(5)
    screenshot_path = context.screenshot
    context.logger.info(f"Screenshot saved at: {screenshot_path}")

    if Counter(categoryNames) == Counter(expected_categories):
        context.logger.info("Assertion pass: all the expected categories are present at the navigation bar")
        assert True 
    else:
        context.logger.info("Assertion FAIL: There is a missmatch between the expected categories and the current ones at the top navigation bar")
        assert False
        
       
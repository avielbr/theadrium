from selenium import webdriver
from selenium.webdriver import ActionChains
import locators as element
from touchers import Touchers as Touch
from credentials import Credentials as Cred


def navigate(course):
    # login page
    page = 'https://yedion.jce.ac.il/yedion/fireflyweb.aspx?prgname=login'

    # running driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(page)

    cursor = ActionChains(driver)

    # logging in
    Touch(driver).fill_by_id(element.ID.USERFIELD, Cred.USERNAME)
    Touch(driver).fill_by_id(element.ID.PASSFIELD, Cred.PASSWORD)
    Touch(driver).click_by_id(element.ID.LOGIN)

    # handling dropdown
    parent = Touch(driver).find_by_css(element.CSS.COURSESITES)
    child = Touch(driver).find_by_css(element.CSS.ENTERCOURSESITES)
    cursor.move_to_element(parent).move_to_element(child).click().perform()

    # selecting course
    Touch(driver).click_by_name(course)

    #entering zoom page
    Touch(driver).find_by_xpath(element.XPath.GOTOZOOMS).click()

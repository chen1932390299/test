from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_located(*loc, timeout, driver):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(*loc))
    if element:
        return element
    else:
        raise NoSuchElementException(f"not found element {loc} in {timeout} seconds.")


def until_visible_element(timeout, element, driver):
    element = WebDriverWait(driver, timeout).until(EC.visibility_of(element))
    if element:
        return element
    else:
        raise NoSuchElementException(f"not found element {element} in {timeout} seconds.")


def util_visible_elements(timeout, driver, *loc):
    elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(*loc))
    if elements:
        return elements
    else:
        raise NoSuchElementException(f"not found elements by {loc} in dom")


def move_to(element, driver):
    """perform action """
    ActionChains(driver).move_to_element(to_element=element).perform()


def screen(driver, img_path):
    """to save image to img_path"""
    driver.get_screenshot_as_file(img_path)


def select_new_window(driver):
    """to change current window to new window"""
    current_handle = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != current_handle:
            driver.switch_to.window(handle)

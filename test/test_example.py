
import time
import os
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from needle.cases import NeedleTestCase


@pytest.mark.page
def test_example_S2B(needle):
    """Example for comparing page with a mask

    :param NeedleDriver needle: NeedleDriver instance
    :return:
    """

    # Navigate to web page
    needle.driver.get('https://s2bssotest.standardchartered.com/unifiedlogin/v2.0/login/index.html?language=en')
    needle.driver.maximize_window()
   
    needle.driver.find_element_by_id('userid_email-name').send_keys('USER123')
    needle.driver.find_element_by_id('group_id-name').send_keys('PASSWORD123')
    needle.driver.find_element_by_id('-name').click()
    # needle.driver.find_element_by_id('unified_password-name').send_keys('invalid')
    # needle.driver.find_element_by_id('login-btn-name').click()     
   
    # Take a entire page screen diff, ignore the doodle banner
    needle.assert_screenshot('s2b_page', threshold=80)


# @pytest.mark.page
# def test_example_page(needle):
#     """Example for comparing entire pages

#     :param NeedleDriver needle: NeedleDriver instance
#     :return:
#     """

#     # Navigate to web page
#     needle.driver.get('http://localhost:3000/skills')

#     # Take a entire page screen diff
#     needle.assert_screenshot('static_page', threshold=80)


# @pytest.mark.element
# def test_example_element(needle):
#     """Example for comparing individual elements

#     :param NeedleDriver needle: NeedleDriver instance
#     :return:
#     """

#     # Navigate to web page
#     needle.driver.get('https://www.google.com')

#     # Ensure the cursor does not appear in the screenshot
#     footer = needle.driver.find_elements_by_xpath('//div[@class="fbar"]')

#     if footer:
#         footer[0].click()

#     # Take an element screen diff
#     needle.assert_screenshot('search_field', (By.ID, 'tsf'), threshold=80)


# @pytest.mark.cleanup
# def test_cleanup_on_success(needle):
#     """Verify that the --needle-cleanup-on-success removes the newly generated file

#     :param NeedleDriver needle: NeedleDriver instance
#     :return:
#     """

#     screenshot_path = os.path.join(needle.output_dir, "cleanup_test.png")

#     # Set cleanup on success to true
#     needle.cleanup_on_success = True

#     # Navigate to web page
#     needle.driver.get('http://localhost:3000/skills')

#     # Take a entire page screen diff
#     needle.assert_screenshot('cleanup_test', threshold=80)

#     assert not os.path.exists(screenshot_path)


# @pytest.mark.output_dir
# def test_output_dir(needle):
#     """Verify that the --needle-output-dir saves the fresh image in the specified directory

#     :param NeedleDriver needle: NeedleDriver instance
#     :return:
#     """

#     # Reassign output_dir
#     needle.output_dir = os.path.join(needle.output_dir, 'extra')
#     needle._create_dir(needle.output_dir)

#     screenshot_path = os.path.join(needle.output_dir, "output_dir_test.png")

#     # Navigate to web page
#     needle.driver.get('http://localhost:3000/skills')

#     # Take a entire page screen diff
#     needle.assert_screenshot('output_dir_test', threshold=80)

#     if not needle.save_baseline:
#         assert os.path.exists(screenshot_path)


# # @pytest.mark.baseline_dir
# # def test_baseline_dir(needle):
# #     """Verify that the --needle-baseline-dir saves the fresh image in the specified directory

# #     :param NeedleDriver needle: NeedleDriver instance
# #     :return:
# #     """

# #     # Reassign output_dir
# #     needle.baseline_dir = os.path.join(needle.baseline_dir, 'default')
# #     needle._create_dir(needle.baseline_dir)

# #     screenshot_path = os.path.join(needle.baseline_dir, "baseline_dir_test.png")

# #     # Navigate to web page
# #     needle.driver.get('http://localhost:3000/skills')

# #     # Take a entire page screen diff
# #     needle.assert_screenshot('baseline_dir_test', threshold=80)

# #     assert os.path.exists(screenshot_path)


# @pytest.mark.viewport
# def test_viewport_size(needle):
#     """Verify that viewport size can be

#     :param NeedleDriver needle: NeedleDriver instance
#     :return:
#     """

#     original_size = needle.driver.get_window_size()

#     needle.viewport_size = "900x600"
#     needle.set_viewport()

#     assert needle.driver.get_window_size() != original_size


# @pytest.mark.engine
# @pytest.mark.parametrize('engine', ('pil', 'perceptualdiff', 'imagemagick'))
# def test_image_engine(needle, engine):
#     """Verify all image engines can be set

#     :param NeedleDriver needle: NeedleDriver instance
#     :return:
#     """

#     needle.engine_class = engine
#     assert needle.engine_class == needle.ENGINES[engine]

#     # Navigate to web page
#     needle.driver.get('http://localhost:3000/skills')

#     # Take a entire page screen diff
#     needle.assert_screenshot('test_' + engine, threshold=80)

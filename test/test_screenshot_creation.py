# """test_screenshot_creation
# """

# import os
# import pytest


# def test_screenshot_creation(needle):
#     """Verify that fresh images are generated regardless if there are baselines

#     :param needle:
#     :return:
#     """

#     if needle.save_baseline:
#         pytest.skip('Only run screenshot creation for non-baseline runs')

#     screenshot_name = 'screenshot_without_baseline'
#     screenshot_path = os.path.join(needle.output_dir, screenshot_name+".png")
#     needle.driver.get('http://localhost:3000/skills')

#     try:
#         needle.assert_screenshot(screenshot_name)
#     except IOError:
#         pass

#     assert os.path.isfile(screenshot_path), "Fresh screenshot was not created (there is no baseline image)"

import os
import time

def take_screenshot(driver, name="screenshot"):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_dir = "screenshots"

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    file_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(file_path)
    return file_path

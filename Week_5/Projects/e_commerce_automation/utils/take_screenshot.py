# Function for screenshot
def take_screenshot(driver, filename):
    i = 1
    while True:
        if not os.path.isfile(f'./screenshots/{filename}{i}.png'):
            driver.save_screenshot(f'./screenshots/{filename}{i}.png')
            print("Screenshot has been saved successfully")
            break
        i += 1
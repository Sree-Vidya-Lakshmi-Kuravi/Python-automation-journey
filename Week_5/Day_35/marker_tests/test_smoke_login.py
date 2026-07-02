import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

## Login test
@pytest.mark.smoke
@pytest.mark.parametrize("username", [("standard_user"), ("locked_out_user"), ("problem_user"), ("performance_glitch_user"), ("error_user"), ("visual_user")])
def test_login(login_fixture, username):
    if username == "locked_out_user":
        msg = login_fixture.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
        print(msg.text)

        assert "locked out" in msg.text, "User logged"
        print("User unable to login")
    
    else:
        assert "inventory" in login_fixture.current_url, "Login failed"
        print("Login success")

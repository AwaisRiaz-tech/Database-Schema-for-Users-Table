**Stack**: Python, Selenium for UI testing.
 
**Question 1: Log in to the site**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
 
def login_to_swag_labs(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    driver.quit()
```
Comment: Ensures that the login process works correctly and verifies redirection to the inventory page.
 
**Question 2: Add item to cart, verify, remove item, and verify**
```python
def add_and_remove_item():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1"
    
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_items) == 0
    driver.quit()
```
Comment: This test case adds and removes an item from the cart and verifies the cart count before and after.
 

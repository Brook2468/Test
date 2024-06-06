import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

sleep_time = 2

@given('the user is on the Sauce Demo login page in Chrome')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(sleep_time)

@given('the user is on the Sauce Demo login page in firefox')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(sleep_time)

@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(sleep_time/2)  
    context.driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(sleep_time/2) 
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(sleep_time) 

@then('the user should be redirected to the products page')
def step_impl(context):
    assert "inventory.html" in context.driver.current_url
    time.sleep(sleep_time)

@when('the user sorts items by price from low to high')
def step_impl(context):
    select = Select(context.driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("lohi")
    time.sleep(sleep_time)

@when('the user adds the first 3 cheapest items to the cart')
def step_impl(context):
    add_to_cart_buttons = context.driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for i in range(3):
        add_to_cart_buttons[i].click()
        time.sleep(sleep_time/2)

@then('the user navigates to the cart page')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(sleep_time)

@then('the user should see 3 items in the cart')
def step_impl(context):
    cart_items = context.driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 3
    time.sleep(sleep_time)

@then('the user proceeds to checkout')
def step_impl(context):
    context.driver.find_element(By.ID, "checkout").click()
    time.sleep(sleep_time)
    context.driver.quit()
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


def test_radio_btn(browser, wait):
    radio_btn_honda = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'input#hondaradio')))
    radio_btn_bmw = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'input#bmwradio')))
    radio_btn_benz = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'input#benzradio')))

    assert not radio_btn_honda.is_selected()
    assert not radio_btn_bmw.is_selected()
    assert not radio_btn_benz.is_selected()

    radio_btn_honda.click()
    assert radio_btn_honda.is_selected()
    assert not radio_btn_bmw.is_selected()
    assert not radio_btn_benz.is_selected()

    radio_btn_bmw.click()
    assert radio_btn_bmw.is_selected()
    assert not radio_btn_honda.is_selected()
    assert not radio_btn_benz.is_selected()

    radio_btn_benz.click()
    ActionChains(browser).double_click(radio_btn_benz).double_click()
    assert radio_btn_benz.is_selected()
    assert not radio_btn_honda.is_selected()
    assert not radio_btn_bmw.is_selected()


def test_checkbox(browser, wait):
    checkbox_honda = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "input#hondacheck")))
    checkbox_benz = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'input#benzcheck')))
    checkbox_bmw = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'input#bmwcheck')))

    assert not checkbox_honda.is_selected()
    assert not checkbox_bmw.is_selected()
    assert not checkbox_benz.is_selected()

    checkbox_honda.click()
    checkbox_bmw.click()
    checkbox_benz.click()

    assert checkbox_honda.is_selected()
    assert checkbox_bmw.is_selected()
    assert checkbox_benz.is_selected()
    checkbox_honda.click()
    assert not checkbox_honda.is_selected()
    assert checkbox_bmw.is_selected()
    assert checkbox_benz.is_selected()
    checkbox_bmw.click()
    checkbox_benz.click()
    assert not checkbox_honda.is_selected()
    assert not checkbox_bmw.is_selected()
    assert not checkbox_benz.is_selected()


def test_switch_window(browser, wait):
    switch_window = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button#openwindow")))
    switch_window.click()
    wait.until(expected_conditions.number_of_windows_to_be(2))
    original_handle = browser.current_window_handle
    new_handle = browser.window_handles[1]
    browser.switch_to.window(new_handle)
    assert original_handle != new_handle
    assert browser.current_url != 'https://courses.letskodeit.com/practice'
    browser.switch_to.window(original_handle)


def test_switch_tab(browser, wait):
    initial_handles = browser.window_handles
    switch_tab = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a#opentab")))
    switch_tab.click()
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    assert browser.current_url != 'https://courses.letskodeit.com/practice'
    browser.close()
    browser.switch_to.window(initial_handles[0])
    assert browser.current_url == 'https://courses.letskodeit.com/practice'


def test_drop_down(browser, wait):
    cars = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'select#carselect')))
    drop_down_select = Select(cars)
    assert drop_down_select.first_selected_option.text == 'BMW'
    drop_down_select.select_by_visible_text('Honda')
    selected_option = drop_down_select.first_selected_option
    assert selected_option.text == 'Honda'
    drop_down_select.select_by_visible_text('Benz')
    selected_option = drop_down_select.first_selected_option
    assert selected_option.text == 'Benz'
    drop_down_select.select_by_visible_text('BMW')
    selected_option = drop_down_select.first_selected_option
    assert selected_option.text == 'BMW'


def test_enable_disable(browser, wait):
    input_example = 'Typing enabled'
    enable_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#enabled-button')))
    disable_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#disabled-button')))
    input_field = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#enabled-example-input')))
    assert input_field.is_enabled()
    input_field.send_keys(input_example)
    assert input_field.get_attribute('value') == input_example
    disable_btn.click()
    assert not input_field.is_enabled()
    enable_btn.click()
    input_field.clear()
    input_field.send_keys('new input')
    assert input_field.get_attribute('value') != input_example


def test_hide_show(browser, wait):
    hide_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#hide-textbox')))
    show_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#show-textbox')))
    input_field = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#displayed-text')))
    assert input_field.is_displayed()
    input_field.send_keys('Hello')
    hide_btn.click()
    assert not input_field.is_displayed()
    show_btn.click()
    assert input_field.is_displayed()
    assert input_field.get_attribute('value') == 'Hello'


def test_alert(browser, wait):
    name = 'Lucy'
    nickname = 'lucy.a'
    alert_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#alertbtn')))
    confirm_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#confirmbtn')))
    input_field = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[name = "enter-name"]')))
    input_field.send_keys(name)
    alert_btn.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    assert alert_text == f'Hello {name}, share this practice page and share your knowledge'
    alert.accept()
    input_field.send_keys(nickname)
    confirm_btn.click()
    alert_text = alert.text
    assert alert_text == f'Hello {nickname}, Are you sure you want to confirm?'
    alert.dismiss()


def test_hover(browser, wait):
    driver = browser
    mouse_hover = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'button#mousehover')))
    driver.execute_script("arguments[0].scrollIntoView();", mouse_hover)
    btn = driver.find_element(By.CSS_SELECTOR, "input#hondacheck")
    btn.click()
    assert btn.is_selected()
    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover).perform()
    driver.find_element(By.CSS_SELECTOR, 'div.mouse-hover-content>:nth-child(2)').click()
    assert not wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"input#hondacheck"))).is_selected()


def test_iframe(browser, wait):
    iframe = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "iframe#courses-iframe")))
    browser.switch_to.frame(iframe)
    search_box = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#search.form-control.find-input.dynamic-text')))
    btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.find-course.search-course")))
    search_box.send_keys('python')
    btn.click()

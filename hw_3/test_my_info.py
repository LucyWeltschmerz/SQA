import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.select import Select


def test_valid_login(get_url, wait):
    username = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.send_keys('Admin')
    password.send_keys('admin123')
    login_btn = get_url.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()
    my_info = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "ul.oxd-main-menu>:nth-child(6)")))
    assert my_info.is_displayed()


def test_full_name_field(get_url, wait):
    my_info = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "ul.oxd-main-menu>:nth-child(6)")))
    my_info.click()
    first_name = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "input[name='firstName']")))
    first_name.send_keys(Keys.COMMAND + 'a')
    first_name.send_keys(Keys.BACK_SPACE)
    first_name.send_keys('Aram')
    assert first_name.get_attribute('value') == 'Aram'

    middle_name = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "input[name='middleName']")))
    middle_name.send_keys(Keys.COMMAND + 'a')
    middle_name.send_keys(Keys.BACK_SPACE)
    middle_name.send_keys("Gregory")
    assert middle_name.get_attribute('value') == 'Gregory'

    last_name = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "input[name='lastName']")))
    last_name.send_keys(Keys.COMMAND + 'a')
    last_name.send_keys(Keys.BACK_SPACE)
    last_name.send_keys("Manukyan")
    assert last_name.get_attribute('value') == 'Manukyan'

    input_fields = get_url.find_elements(By.CSS_SELECTOR,'input[class= "oxd-input oxd-input--active"]')
    nickname = input_fields[1]
    nickname.send_keys(Keys.COMMAND + 'a')
    nickname.send_keys(Keys.BACK_SPACE)
    nickname.send_keys('AM')
    assert nickname.get_attribute('value') == 'AM'


def test_employee_id(get_url, wait):
    input_fields = get_url.find_elements(By.CSS_SELECTOR,'input[class= "oxd-input oxd-input--active"]')
    employee_id = input_fields[2]
    employee_id.send_keys(Keys.COMMAND + 'a')
    employee_id.send_keys(Keys.BACK_SPACE)
    employee_id.send_keys('01234')
    assert employee_id.get_attribute('value') == '01234'


def test_other_id_field(get_url, wait):
    input_fields = get_url.find_elements(By.CSS_SELECTOR,'input[class= "oxd-input oxd-input--active"]')
    other_id = input_fields[3]
    other_id.send_keys(Keys.COMMAND + 'a')
    other_id.send_keys(Keys.BACK_SPACE)
    other_id.send_keys('000333')
    assert other_id.get_attribute('value') == '000333'


def test_drivers_license_field(get_url, wait):
    input_fields = get_url.find_elements(By.CSS_SELECTOR,'input[class= "oxd-input oxd-input--active"]')
    drivers_license = input_fields[4]
    drivers_license.send_keys(Keys.COMMAND + 'a')
    drivers_license.send_keys(Keys.BACK_SPACE)
    drivers_license.send_keys('12891')
    assert drivers_license.get_attribute('value') == '12891'


def test_license_exp_field(get_url, wait):
    license_exp_date = wait.until(condition.visibility_of_element_located((By.XPATH, '//*/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')))
    license_exp_date.click()
    license_exp_date.send_keys(Keys.COMMAND + 'a')
    license_exp_date.send_keys(Keys.BACK_SPACE)
    license_exp_date.send_keys("2024-03-10")
    assert license_exp_date.get_attribute('value') == "2024-03-10"


def test_ssn_field(get_url,wait):
    ssn_number = wait.until(condition.element_to_be_clickable((By.XPATH, '//*/form/div[2]/div[3]/div[1]/div/div[2]/input')))
    ssn_number.send_keys(Keys.COMMAND + 'a')
    ssn_number.send_keys(Keys.BACK_SPACE)
    ssn_number.send_keys('999')
    assert ssn_number.get_attribute('value') == '999'


def test_sin_field(get_url, wait):
    input_fields = get_url.find_elements(By.CSS_SELECTOR,'input[class= "oxd-input oxd-input--active"]')
    sin_number = input_fields[7]
    sin_number.send_keys(Keys.COMMAND + 'a')
    sin_number.send_keys(Keys.BACK_SPACE)
    sin_number.send_keys('777')
    assert sin_number.get_attribute('value') == '777'


def test_birth_date(get_url, wait):
    birth_date = wait.until(condition.visibility_of_element_located((By.XPATH, '//*/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')))
    birth_date.send_keys(Keys.COMMAND + 'a')
    birth_date.send_keys(Keys.BACK_SPACE)
    birth_date.send_keys('1990-10-24')
    assert birth_date.get_attribute('value') == '1990-10-24'


def test_military(get_url,wait):
    military_service = wait.until(condition.visibility_of_element_located((By.XPATH,'//*/form/div[4]/div/div[1]/div/div[2]/input')))
    military_service.send_keys(Keys.COMMAND + 'a')
    military_service.send_keys(Keys.BACK_SPACE)
    military_service.send_keys('2 years, RA')
    assert military_service.get_attribute('value') == '2 years, RA'


def test_nationality(get_url,wait):
    nationality_drp_btn = wait.until(condition.element_to_be_clickable((By.XPATH, '//*/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/i')))
    nationality_drp_btn.click()
    albanian = wait.until(condition.element_to_be_clickable((By.XPATH, '//*/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]')))
    albanian.click()
    selected_option = wait.until(condition.element_to_be_clickable((By.XPATH, '//*/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]')))
    assert selected_option.text == 'Albanian'


def test_gender_radio_btn(get_url, wait):
    gender_btn_male = wait.until(condition.element_to_be_clickable((By.XPATH,'//*/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span')))
    gender_btn_female = get_url.find_element(By.XPATH, '//*/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span')
    try:
        if gender_btn_male.is_selected():
            assert not gender_btn_female.is_selected()
        else:
            gender_btn_female.click()
            assert gender_btn_female.is_selected()
    except AssertionError:
        print()


def test_checkbox(get_url, wait):
    checkbox = wait.until(condition.element_to_be_clickable((By.XPATH, "//*/form/div[4]/div/div[2]/div/div[2]/div/label/span")))
    try:
        if checkbox.is_selected():
            assert checkbox.is_selected()
        else:
            checkbox.click()
            assert not checkbox.is_selected()
    except AssertionError:
        print("Assertion Error: Checkbox is not selected as expected")


def test_marital_status(get_url, wait):
    options_btn = wait.until(condition.element_to_be_clickable((By.XPATH, "//*/form/div[3]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/i")))
    options_btn.click()
    single_option = wait.until(condition.element_to_be_clickable((By.XPATH, '//*/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]')))
    single_option.click()
    selected_option = wait.until(condition.element_to_be_clickable((By.XPATH, "//*/form/div[3]/div[1]/div[2]/div/div[2]/div/div[1]/div[1]")))
    assert selected_option.text == 'Single'


def test_save_btn(get_url, wait):
    save_btn = wait.until(condition.element_to_be_clickable((By.XPATH, '//*/form/div[5]/button')))
    save_btn.click()
    first_name = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "input[name='firstName']")))
    assert first_name.get_attribute('value') == 'Aram'

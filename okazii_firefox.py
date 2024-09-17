# ##TEST CASE
# ## PLAN DE TESTARE


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests

#SETUP FOR BROWSER

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_homepage_status():
    url = "https://www.okazii.ro/"
    response = requests.get(url)

    # VERIFYING CODE OF STATUS HTTP

    assert response.status_code == 200, f"The status code is {response.status_code}, we are waiting 200"

    # VERIFYING LENGTH OF THE ANSWER

    assert len(response.text) > 0, "The response content is empty"


# TEST FOR SEARCH-BAR ON SITE

def test_shopping_cart(browser):
    browser = webdriver.Firefox()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    # try:
        #CLOSE THE COOKIE TAB

    cookie_element = browser.find_element(By.CSS_SELECTOR,"#cookiescript_buttons > div:nth-child(3)")
    cookie_element.click()
    time.sleep(3)

        #SEARCH IN THE SEARCH-BAR

    search_bar = browser.find_element(By.CSS_SELECTOR, "#terms")
    search_bar.send_keys("husa iphone 15 pro max")
    time.sleep(2)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)

    # actions = ActionChains(browser)
    # actions.send_keys(Keys.PAGE_DOWN).perform()
    # for _ in range(1):  
    #        actions.send_keys(Keys.PAGE_DOWN).perform()
    #        time.sleep(2)
    choose_mark = browser.find_element(By.CSS_SELECTOR, "label.attributeOption:nth-child(1) > a:nth-child(2)")
    choose_mark.click()
    time.sleep(4)

    # actions = ActionChains(browser)
    # actions.send_keys(Keys.PAGE_DOWN).perform()
    # for _ in range(1):  
    #        actions.send_keys(Keys.PAGE_DOWN).perform()
    # time.sleep(2)

    choose_price = browser.find_element(By.ID, "pret_min")
    choose_price.send_keys("123")
    time.sleep(2)

    price_max = browser.find_element(By.ID, "pret_max")
    price_max.send_keys("321")
    time.sleep(2)
    price_max.send_keys(Keys.RETURN)
    time.sleep(2)

    choose_product = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[3]/div[1]/h2/a")
    choose_product.click()
    time.sleep(2)

    add_to_cart = browser.find_element(By.ID, "btn_addProductToCart")
    add_to_cart.click()
    time.sleep(2)

    add_to_cart_part_2 = browser.find_element(By.XPATH, "/html/body/div[13]/div[1]/div/div/div[2]/div[1]/div[3]/a")
    add_to_cart_part_2.click()
    time.sleep(2)

    set_amount = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div/ul/li/div/div[2]/div[1]/div/div[2]/button")
    set_amount.click()
    time.sleep(2)
    
    go_to_delivery_dates = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/button")
    go_to_delivery_dates.click()
    time.sleep(2)

    first_name = browser.find_element(By.ID, "u-address_firstname")
    first_name.send_keys("Marian")
    time.sleep(2)

    surname = browser.find_element(By.ID, "u-address_lastname")
    surname.send_keys("Dobrota")
    time.sleep(2)

    phone_number = browser.find_element(By.ID, "u-address_mobile")
    phone_number.send_keys("0770070711")
    time.sleep(2)

    email = browser.find_element(By.ID, "u-address_email")
    email.send_keys("mariandobrota00@yahoo.org")
    time.sleep(2)

    county = browser.find_element(By.ID, "u-address_county")
    county.send_keys("p")
    time.sleep(2)
    county.send_keys(Keys.RETURN)
    time.sleep(2)

    city = browser.find_element(By.ID, "u-address_city" )
    city.send_keys("a" * 7)
    time.sleep(2)

    street_name = browser.find_element(By.ID, "u-address_street")
    street_name.send_keys("Strada Alunisului")
    time.sleep(2)

    number_of_the_street = browser.find_element(By.ID, "u-address_number")
    number_of_the_street.send_keys("11")
    time.sleep(2)

    zipcode = browser.find_element(By.ID, "u-address_zipcode")
    zipcode.send_keys("770016")
    time.sleep(2)

    checkout = browser.find_element(By.CSS_SELECTOR, "span.large")
    checkout.click()
    time.sleep(2)

    pay_with_card_box = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div[3]/div[1]/div[3]/label")
    pay_with_card_box.click()
    time.sleep(2)

    place_the_order = browser.find_element(By.ID, "button-progress")
    place_the_order.click()
    time.sleep(7)

    card_name = browser.find_element(By.ID, "CardName")
    card_name.send_keys("Marian Dobrota")
    time.sleep(2)

    card_number = browser.find_element(By.ID,"CardNumber")
    card_number.send_keys("0101")
    card_number.send_keys("0000")
    card_number.send_keys("3333")
    card_number.send_keys("4444")
    time.sleep(2)

    card_validity = browser.find_element(By.ID, "expirare")
    card_validity.send_keys("11")
    card_validity.send_keys("28")
    time.sleep(2)

    cvv_card = browser.find_element(By.ID, "cvc2")
    cvv_card.send_keys("606")
    time.sleep(2)

    phone_number_2 = browser.find_element(By.ID, "Telefon")
    phone_number_2.send_keys("0770070711")
    time.sleep(2)

    agree_tc = browser.find_element(By.ID, "acordTermeni")
    agree_tc.click()
    time.sleep(2)

#TEST FOR PART OF LOGIN

def test_login(browser):
    browser = webdriver.Firefox()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:


        cookie_element = browser.find_element(By.CSS_SELECTOR,"#cookiescript_buttons > div:nth-child(3)")
        cookie_element.click()
        time.sleep(3)

        login = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div[1]/a/span[2]")
        login.click()
        time.sleep(2)

        email_login = browser.find_element(By.ID, "login_input")
        email_login.send_keys("florinaiulianardelean@gmail.com")
        time.sleep(2)

        password_login = browser.find_element(By.ID, "login_pass")
        password_login.send_keys("marianputernicul1")
        time.sleep(2)

        login2 = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div[2]/form/div[4]/button")
        login2.click()
        time.sleep(2)

        assert "Bine ai venit" in browser.page_source

    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


#TEST FOR ADD AT FAVORITES

def test_favorites(browser):
    browser = webdriver.Firefox()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:

        cookie_element = browser.find_element(By.CSS_SELECTOR,"#cookiescript_buttons > div:nth-child(3)")
        cookie_element.click()
        time.sleep(3)

        login = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div[1]/a/span[2]")
        login.click()
        time.sleep(2)

        email_login = browser.find_element(By.ID, "login_input")
        email_login.send_keys("florinaiulianardelean@gmail.com")
        time.sleep(2)

        password_login = browser.find_element(By.ID, "login_pass")
        password_login.send_keys("marianputernicul1")
        time.sleep(2)

        login2 = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div[2]/form/div[4]/button")
        login2.click()
        time.sleep(2)

        search_bar = browser.find_element(By.CSS_SELECTOR, "#terms")
        search_bar.send_keys("baterie externa")
        time.sleep(2)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)

        add_favorites = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[4]/div/div[2]/div/ul/div/div/li[1]")
        add_favorites.click()
        time.sleep(2)

        add_favorites_2 = browser.find_element(By.ID, "btn_addToWatchList")
        add_favorites_2.click()
        time.sleep(4)

        close_popup = browser.find_element(By.XPATH, "/html/body/div[10]/div/div/form/div[2]/div/button")
        close_popup.click()
        time.sleep(2)

        go_to_favorites = browser.find_element(By.CSS_SELECTOR, "a.with-notifier")
        go_to_favorites.click()
        time.sleep(2)

        select_product = browser.find_element(By.ID, "auction_234594171")
        select_product.click()
        time.sleep(2)

        # delete_from_favorites = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div/div[1]/form/div[2]/span[1]/input[3]")
        # delete_from_favorites.click()
        # time.sleep(2)
        # delete_from_favorites.send_keys(Keys.RETURN)
        # time.sleep(2)






    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


#TEST FOR FUNCTIONABILITY URL-s

def test_functionability_links(browser):
    browser = webdriver.Firefox()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:

        cookie_element = browser.find_element(By.CSS_SELECTOR,"#cookiescript_buttons > div:nth-child(3)")
        cookie_element.click()
        time.sleep(3)
        actions = ActionChains(browser)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        for _ in range(10):  
            actions.send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(3)

        redirect_link = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div[4]/ul/li/a")
        redirect_link.click()
        time.sleep(2)

        libra_pay = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/ul/li[1]/div")
        libra_pay.click()
        time.sleep(2)

        accept_cookies_2 = browser.find_element(By.CSS_SELECTOR, ".cookie-consent-block")
        accept_cookies_2.click()
        time.sleep(2)


        assert "LibraPay" in browser.page_source
   
    
    
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")

 #TEST SITE PROTOCOL

def test_protocol(browser):
    browser = webdriver.Firefox()
    browser.maximize_window()

    browser.get("https://www.okazii.ro/")
    time.sleep(3)

    try:
   
        browser.get("https://www.okazii.ro/")
        
        browser.implicitly_wait(10)
        

    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")













   
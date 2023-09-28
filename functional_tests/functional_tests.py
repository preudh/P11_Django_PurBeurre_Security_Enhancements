import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# path to chromedriver.exe, use the correct path for your computer and your version of Chrome (windows here)
driver_path = "C:/ProjetsOC/P8/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service = service)

# Maximize the browser window
driver.maximize_window()


class UserTasks:
    def __init__(self):
        self.driver = driver

    def test_register(self):
        #  Verify Customer Registration
        # Test name: register
        # Step # | name | target | value
        # 1 | open | /login/ |
        self.driver.get("http://127.0.0.1:8000/login/")
        # 2 | click | linkText=Créer un compte |
        self.driver.find_element(By.LINK_TEXT, "Créer un compte").click()
        time.sleep(1)
        # 3 | type | id=id_username | michele
        self.driver.find_element(By.ID, "id_username").send_keys("michele")
        time.sleep(1)
        # 4 | click | id=id_email |
        self.driver.find_element(By.ID, "id_email").click()
        time.sleep(1)
        # 5 | type | id=id_email | michele@gmail.com
        self.driver.find_element(By.ID, "id_email").send_keys("michele@gmail.com")
        time.sleep(1)
        # 6 | click | id=id_password1 |
        self.driver.find_element(By.ID, "id_password1").click()
        time.sleep(1)
        # 7 | type | id=id_password1 | 58Au2xNpG
        self.driver.find_element(By.ID, "id_password1").send_keys("58Au2xNpG")
        time.sleep(1)
        # 8 | click | id=id_password2 |
        self.driver.find_element(By.ID, "id_password2").click()
        time.sleep(1)
        # 9 | type | id=id_password2 | 58Au2xNpG
        self.driver.find_element(By.ID, "id_password2").send_keys("58Au2xNpG")
        time.sleep(1)
        # 10 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

    def test_enter_login(self):
        #  Verify Login Functionality
        # Test name: enter_login
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(1)
        # 2 | click | css=.fa-user-alt |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-user-alt").click()
        time.sleep(1)
        # 3 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 4 | type | id=id_username | patoche
        self.driver.find_element(By.ID, "id_username").send_keys("michele")
        time.sleep(1)
        # 5 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        time.sleep(1)
        # 6 | type | id=id_password | 58Au2xNpV
        self.driver.find_element(By.ID, "id_password").send_keys("58Au2xNpG")
        time.sleep(1)
        # 7 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

    def test_search(self):
        # verify input search with category ou product redirect to substitutes pages
        # Test name: search
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(1)
        # 2 | click | id=myAutocomplete |
        self.driver.find_element(By.ID, "myAutocomplete").click()
        # 3 | type | id=myAutocomplete | Viandes
        self.driver.find_element(By.ID, "myAutocomplete").send_keys("Viandes")
        time.sleep(3)
        # 4 | click | css=.input-group:nth-child(3) > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(3) > .btn").click()
        time.sleep(3)
        # to pagination

    def test_save(self):
        self.driver.get("http://127.0.0.1:8000/search/?search=Viandes")
        time.sleep(3)
        self.driver.find_element(By.ID, "myAutocomplete").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "myAutocomplete").send_keys("Viandes")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(5) .fas").click()
        time.sleep(3)

    def test_detail(self):
        # Test name: detail
        # Step # | name | target | value
        # 1 | open | /detail/496 |
        self.driver.get("http://127.0.0.1:8000/detail/2358")
        time.sleep(1)
        # 2 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

    def test_favorite(self):
        # Test name: favorite
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(3)
        # 2 | click | css=.fa-carrot |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-carrot").click()
        time.sleep(3)

    def test_remove_favorite(self):
        # Test name: test_remove_favorite
        # Step # | name | target | value
        # 1 | open | /favorite/ |
        self.driver.get("http://127.0.0.1:8000/favorite/")
        time.sleep(3)
        # 2 | click | css=tr:nth-child(1) .btn |
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)

    def test_logout(self):
        # Test name: test_logout
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(3)
        # 2 | click | css=.fa-sign-out-alt |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        time.sleep(3)

    def test_password_reset(self):
        self.driver.get("http://127.0.0.1:8000/password_reset/")
        time.sleep(1)

        # enter email address to reset password
        self.driver.find_element(By.ID, "id_email").send_keys("test@example.com")
        time.sleep(1)

        # clik on the button to reset password
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

        # At this stage, you should check the Django console for the password reset link.
        # Copy this link and use it in the script below.
        # Note: You will probably have to do this manually each time, as the URL will contain a unique token.

    def test_password_reset_confirm(self):
        # use the link from the console to open the password reset page
        # Replace <uidb64> and <token> with the actual values

        reset_link = "http://127.0.0.1:8000/reset/<uidb64>/<token>/"
        self.driver.get(reset_link)
        time.sleep(1)

        # Enter the new password
        self.driver.find_element(By.ID, "id_new_password1").send_keys("NewPassword123")
        time.sleep(1)

        # Confirm the new password
        self.driver.find_element(By.ID, "id_new_password2").send_keys("NewPassword123")
        time.sleep(1)

        # Click on the button to confirm the new password
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

    def launch_test(self):
        """Test scenario"""
        self.test_register()
        self.test_enter_login()
        self.test_search()
        self.test_save()
        self.test_detail()
        self.test_favorite()
        self.test_remove_favorite()
        self.test_logout()
        self.test_password_reset()
        self.test_password_reset_confirm()


userstories = UserTasks()
userstories.launch_test()

# Close the browser window
driver.quit()

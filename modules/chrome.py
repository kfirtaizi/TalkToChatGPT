import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from modules.utils import get_chrome_profile_path


class ChromeHandler:
    def __init__(self, driver=None):
        self.driver = driver
        self.current_last_div = None

    def get_last_message(self):
        parent_div_xpath = '/html/body/div/div/div[1]/main/div[1]/div/div/div'
        parent_div = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, parent_div_xpath)))
        try:
            last_answer_div = parent_div.find_elements(by=By.XPATH, value='./*')[-2]
        except Exception:
            last_answer_div = parent_div.find_elements(by=By.XPATH, value='./*')[-1]
        return last_answer_div.text

    def send_question(self, question):
        message_textbox_xpath = '/html/body/div/div/div[1]/main/div[2]/form/div/div[2]/textarea'
        message_textbox = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, message_textbox_xpath)))
        self.current_last_div = self.get_last_message()
        message_textbox.send_keys(question, Keys.ENTER)

    def get_answer(self):
        return self.get_last_message()

    def launch_browser_by_profile(self, profile_name):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument(f"--user-data-dir={get_chrome_profile_path(profile_name)}")
        # options.add_argument("--headless")

        try:
            self.driver = uc.Chrome(options=options)
        except Exception:
            return None

        url = "https://chat.openai.com/chat"
        self.driver.get(url)
        return self.driver

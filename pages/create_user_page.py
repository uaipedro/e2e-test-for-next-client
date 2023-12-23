class CreateUserPage:
    def __init__(self, driver) -> None:
        self.base_url = "https://next-client-with-login.vercel.app/singin"
        self.driver = driver
        pass

    def load(self):
        self.driver.get(self.base_url)
        pass

    def fill_form(self, usuario, email, senha):
        self.driver.find_element("id", "username").send_keys(usuario)
        self.driver.find_element("id", "email").send_keys(email)
        self.driver.find_element("id", "password").send_keys(senha)
        self.driver.find_element("id", "confirmPassword").send_keys(senha)
        pass

    def submit_form(self):
        self.driver.find_element("xpath", "//button[@type='submit']").click()

    def get_error_message(self):
        try:
            return self.driver.find_element("css selector", ".error").text.lower()
        except Exception:
            return ""

    def get_input_validation_message(self, field_name):
        try:
            return self.driver.find_element(
                "xpath", f"//input[@id='{field_name}']"
            ).get_attribute("validationMessage")
        except Exception:
            return ""

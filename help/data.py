import allure

class Data:
   
    @staticmethod
    @allure.step("Вывод email тестового пользователя")
    def get_test_user_email():
        return "prikolprikolov@gmail.com"

    @staticmethod
    @allure.step("Вывод пароля тестового пользователя")
    def get_test_user_password():
        return "prikol"


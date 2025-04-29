from selenium.webdriver.common.by import By


class Locators:
    #1 кнопка входа в личный кабинет
    ENTRANCE_ACCOUNT_BUTTON = [By.XPATH, ".//p[text()='Личный Кабинет']"]

    #2 переход на форму регистрации
    REGISTRATION_FORM_LINK = [By.XPATH, ".//a[text()='Зарегистрироваться']"]

    #3 поле ввода имени в форме регистрации
    NAME_INPUT_FIELD = [By.XPATH, "(.//input[@class='text input__textfield text_type_main-default'])[1]"]

    #4 поле ввода email в форме регистрации
    EMAIL_INPUT_FIELD = [By.XPATH, "(.//input[@class='text input__textfield text_type_main-default'])[2]"]

    #5 поле ввода пароля в форме регистрации
    PASSWORD_INPUT_FIELD = [By.CSS_SELECTOR, "html input[name='Пароль']"]

    #6 кнопка "Зарегистрироваться" в форме регистрации
    REGISTRATION_BUTTON = [By.XPATH, ".//button[text()='Зарегистрироваться']"]

    #7 кнопка "Войти в аккаунт" на главной
    BUTTON_ENTRANCE_ACCAUNT = [By.CSS_SELECTOR, "html button[class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"]

    #8 кнопка "Войти" форме входа
    BUTTON_ENTRANCE = [By.XPATH, ".//button[text()='Войти']"]

    #9 ссылка на восстановить пароль
    BUTTON_RECOVER_PASSWORD = [By.XPATH, ".//a[text()='Восстановить пароль']"]

    #10 кнопка войти в окне восстановления пароля
    BUTTON_ENTRANCE_IN_RECOVER = [By.CSS_SELECTOR, "html a[class='Auth_link__1fOlj']"]

    #11 кнопка Конструктор
    CONSTRUKTOR_BUTTON = [By.XPATH, ".//p[text()='Конструктор']"]

    #12 логотип StellaBurgers
    LOGO = [By.CSS_SELECTOR, "html svg[xmlns='http://www.w3.org/2000/svg']"]

    #13 кнопка Выход в личном кабинете
    EXIT_BUTTON = [By.CSS_SELECTOR, "html button[class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"]

    #14 кнопка Булки
    BREAD_BUTTON = [By.XPATH, ".//main/section[1]/div[1]/div[1]"]

    #15 кнопка Соусы
    SOUCE_BUTTON = [By.XPATH, ".//main/section[1]/div[1]/div[2]"]

    #16 кнопка Начинки
    TOPPING_BUTTON = [By.XPATH, ".//div[contains(text(), 'Начинки')]"]

    #17 text wrong password
    SHORT_PASSWORD = [By.CSS_SELECTOR, "html p[class='input__error text_type_main-default']"]

    #18 кнопка оформить заказ
    MAKE_ORDER_BUTTON = [By.XPATH, ".//button[text()='Оформить заказ']"]

    #19 поле ввода email в форме регистрации
    EMAIL_INPUT_FIELD_ENTRANCE = [By.XPATH, "(.//input[@class='text input__textfield text_type_main-default'])[1]"]

    #20 поле ввода пароль в форме регистрации
    PASSWORD_INPUT_FIELD_ENTRANCE = [By.XPATH, "(.//input[@class='text input__textfield text_type_main-default'])[2]"]

    #21 кнопка войти на форме регистрации
    ENTRANCE_ACCOUNT_BUTTON_IN_REGISTRATION_FORM = [By.XPATH, ".//a[@class ='Auth_link__1fOlj']"]

    #22 кнопка "Зарегистрироваться" в форме на входе в личный кабинет
    REGISTRATION_BUTTON_IN_ENTRANCE_FORM = [By.XPATH, ".//a[text()='Зарегистрироваться']"]

    #23 кнопка профиль в ЛК
    PROFILE = [By.CSS_SELECTOR, "html a[class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"]

    #24 кнопка "Войти" при вводе логина и пароля
    BUTTON_ENTRANCE_ACCAUNT_LOGIN = [By.CSS_SELECTOR, "html button[class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]

    #25 text Соберите бургер
    CONSTRUKT_YOUR_BURGER = [By.CSS_SELECTOR, "html h1[class='text text_type_main-large mb-5 mt-10']"]
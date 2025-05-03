from selenium.webdriver.common.by import By


class Locators:
    #1 кнопка входа в личный кабинет
    ENTRANCE_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    #2 переход на форму регистрации
    REGISTRATION_FORM_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    #3 поле ввода имени в форме регистрации
    NAME_INPUT_FIELD = (By.XPATH, ".//div[label[contains(text(),'Имя')]]//input")

    #4 поле ввода email в форме регистрации
    EMAIL_INPUT_FIELD = (By.XPATH, ".//div[label[contains(text(),'Email')]]//input")

    #5 поле ввода пароля в форме регистрации
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='Пароль']")

    #6 кнопка "Зарегистрироваться" в форме регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    #7 кнопка "Войти в аккаунт" на главной
    BUTTON_ENTRANCE_ACCAUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    #8 кнопка "Войти" форме входа
    BUTTON_ENTRANCE = (By.XPATH, ".//button[text()='Войти']")

    #9 ссылка на восстановить пароль
    BUTTON_RECOVER_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")

    #10 кнопка войти в окне восстановления пароля
    BUTTON_ENTRANCE_IN_RECOVER = (By.XPATH, ".//a[text()='Войти']")

    #11 кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")

    #12 логотип StellaBurgers
    LOGO = (By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']")

    #13 кнопка Выход в личном кабинете
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    #14 кнопка Булки
    BREAD_BUTTON = (By.XPATH, "//span[text()='Булки']")

    #15 кнопка Соусы
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']")

    #16 кнопка Начинки
    TOPPING_BUTTON = (By.XPATH, "//span[text()='Начинки']")

    #17 text wrong password
    SHORT_PASSWORD = (By.CSS_SELECTOR, "p.input__error")

    #18 кнопка оформить заказ
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    #19 поле ввода email в форме входа в ЛК
    EMAIL_INPUT_FIELD_ENTRANCE = (By.XPATH, ".//div[label[contains(text(),'Email')]]//input")

    #20 поле ввода пароль в форме входа в ЛК
    PASSWORD_INPUT_FIELD_ENTRANCE = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")

    #21 кнопка войти на форме регистрации
    ENTRANCE_ACCOUNT_BUTTON_IN_REGISTRATION_FORM = (By.XPATH, ".//a[@class ='Auth_link__1fOlj']")

    #22 кнопка "Зарегистрироваться" в форме на входе в личный кабинет
    REGISTRATION_BUTTON_IN_ENTRANCE_FORM = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    #23 кнопка профиль в ЛК
    PROFILE = (By.XPATH, ".//a[text()='Профиль']")

    #24 text Соберите бургер
    CONSTRUCT_YOUR_BURGER = (By.CSS_SELECTOR, "h1[class='text text_type_main-large mb-5 mt-10']")

    #25 Таб Булки активна
    ACTIVE_BREAD_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Булки']")

    #26 Таб Соусы активна
    ACTIVE_SAUCE_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Соусы']")

    #27 Таб Соусы Начинки
    ACTIVE_TOPPING_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Начинки']")

from selenium.webdriver.common.by import By

class Locators:
    REG_LOGIN_ACCOUNT = (By.XPATH, './/button[text()="Войти в аккаунт"]') #кнопка войти в аккаунт
    REG_LK = (By.XPATH, './/p[text()="Личный Кабинет"]') #кнопка входа в личный кабине
    REG_LOGOUT = (By.XPATH, './/button[text()="Выход"]') # кнопка выхода из аккаунта
    REG_CONSTR = (By.XPATH, './/p[text()="Конструктор"]') # кнопка конструктор
    REG_LOGO = (By.CSS_SELECTOR, '#root > div > header > nav > div') #логотип
    SOUS = (By.XPATH, './/span[text()="Соусы"]/parent::div') # кнопка перехода к выбору соуса
    BREAD = (By.XPATH, './/span[text()="Булки"]/parent::div') # Выбор булки
    FILLING = (By.XPATH, './/span[text()="Начинки"]/parent::div') #выбор начинки
    EMAIL = (By.XPATH, './/label[text()="Email"]/parent::div/input')# ввод мэила
    PASSWORD = (By.XPATH, './/label[text()="Пароль"]/parent::div/input') #ввод пароля
    REG_LOGIN = (By.XPATH, './/button[text()="Войти"]') #кнопка войти
    REGISTRATION = (By.XPATH, './/a[text() ="Зарегистрироваться"]') #кнопка зарегистироваться
    RESTOR_PAS = (By.XPATH, './/a[text()="Восстановить пароль"]') #кнопка восстановить пароль
    REG_LOGIN_A = (By.XPATH, './/a[text()="Войти"]') #войти через регистрацию
    BURGER_CONSTR = (By.XPATH, './/h1[text()="Соберите бургер"]') #надпись соберите бургер
    NAME = (By.XPATH, './/label[text()="Имя"]') #надпись имя
    LOGIN_LABEL = (By.XPATH, './/h2[text()="Вход"]') #надпись вход
    REGISTRATION_TEXT = (By.XPATH, './/h2[text()="Регистрация"]') #надпись регистрация
    RESTORING_PAS = (By.XPATH, './/h2[text()="Восстановление пароля"]') #надпись восстановление пароля в форме
    REG_NAME = (By.XPATH, './/label[text()="Имя"]/parent::div/input') #поле для ввода имени в регистрации
    REG_EMAIL = (By.XPATH, './/label[text()="Email"]/parent::div/input') #поле для ввода мэила
    REG_PAS = (By.XPATH, './/label[text()="Пароль"]/parent::div/input') #поле для ввода пароля
    REGISTR_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]') #кнопка зарегистрироваться в форме регистрации
    PAS_ERROR = (By.XPATH, './/label[text()="Пароль"]/parent::div') #сообщение об ошибке при вводе некорректного пароля

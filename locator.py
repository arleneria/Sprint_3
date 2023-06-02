from selenium.webdriver.common.by import By
class Locators:
    REG_LOGIN_ACCOUNT = (By.XPATH, './/button[text()="Войти в аккаунт"]') #кнопка войти в аккаунт
    REG_LK = (By.XPATH, './/p[text()="Личный Кабинет"]') #кнопка входа в личный кабине
    REG_LOGOUT = (By.XPATH, './/button[text()="Выход"]') # кнопка выхода из аккаунта
    REG_CONSTR = (By.XPATH, './/p[text()="Конструктор"]') # кнопка конструктор
    REG_LOGO = (By.CSS_SELECTOR, '#root > div > header > nav > div') #логотип
    SOUS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]') # кнопка перехода к выбору соуса
    BREAD = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]') # Выбор булки
    FILLING = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]') #выбор начинки
    EMAIL = (By.XPATH, './/label[text()="Email"]/parent::div/input')# ввод мэила
    PASSWORD = (By.XPATH, './/label[text()="Пароль"]/parent::div/input') #ввод пароля
    REG_LOGIN = (By.XPATH, './/button[text()="Войти"]') #кнопка войти
    REGISTRATION = (By.XPATH, './/a[text() ="Зарегистрироваться"]') #кнопка зарегистироваться
    RESTOR_PAS = (By.XPATH, './/a[text()="Восстановить пароль"]') #кнопка восстановить пароль
    REG_LOGIN_A = (By.XPATH, './/a[text()="Войти"]') #войти через регистрацию
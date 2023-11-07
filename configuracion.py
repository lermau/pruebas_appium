from appium import webdriver
def configuracion_celular():
    caps = {
        "appium:platformVersion": "10",
        # "appium:deviceName": "lancelot",
        # "appium:platformVersion": "8",
        # "appium:deviceName": "cereus",
        "appium:deviceName": "doha",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.ine.app",
        # "appium:appActivity": "com.ine.app.modules.main.view.MainActivity",
        "appium:appActivity": "com.ine.app.modules.splash.view.SplashActivity",
        "platformName": "Android",
        "appium:appWaitDuration": 30000,
    }

    print("Iniciando Test03  con Appium")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    # driver.implicitly_wait(30)
    return driver

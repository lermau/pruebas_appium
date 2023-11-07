# import allure
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import misFunciones as mf
# from appium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configuracion as conf

driver = conf.configuracion_celular()
driver.implicitly_wait(30)

# caps = {
#     "appium:platformVersion": "10",
#     # "appium:deviceName": "lancelot",
#     # "appium:platformVersion": "8",
#     # "appium:deviceName": "cereus",
#     "appium:deviceName": "doha",
#     "appium:automationName": "UiAutomator2",
#     "appium:appPackage": "com.ine.app",
#     # "appium:appActivity": "com.ine.app.modules.main.view.MainActivity",
#     "appium:appActivity": "com.ine.app.modules.splash.view.SplashActivity",
#     "platformName": "Android",
#     "appium:appWaitDuration": 30000,
# }
#
# print("Iniciando Test13 Happy Path Actualización con Appium")
# driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
# driver.implicitly_wait(25)
#

def test_longitud_usuario():
    # asignación de permisos
    wait = WebDriverWait(driver, 10)

    boton_ir_configuracion = wait.until(
        EC.presence_of_element_located((
            AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    boton_ir_configuracion.click()

    textoUsuario = driver.find_element(AppiumBy.ID, 'com.ine.app:id/edtLoginUsrname')
    textoUsuario.click()
    # time.sleep(8)
    textoUsuario.send_keys("EN091507")
    # time.sleep(8)
    lon_usuario = len(textoUsuario.text)
    assert lon_usuario >= 8, "No cumple la longitud para usuario"
    # time.sleep(5)


# @pytest.mark.only()
def test_longitud_password():
    wait = WebDriverWait(driver, 10)
    texto_contrasenia = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/edtPassword')))

    texto_contrasenia.click()
    texto_contrasenia.set_text("Passw01.")
    driver.hide_keyboard()
    lon_contrasenia = len(texto_contrasenia.text)
    assert lon_contrasenia >= 8, "No cumple la longitud para password"


# @pytest.mark.only()
def test_terminos_y_condiciones():
    checkTerminos = driver.find_element(AppiumBy.ID, 'com.ine.app:id/check_tyc')
    checkTerminos.click()
    boton_aceptar = driver.find_element(AppiumBy.ID, 'com.ine.app:id/btn_ingresar')
    aceptar_habilitado = boton_aceptar.is_enabled()
    boton_aceptar.click()
    assert aceptar_habilitado


def test_elegir_ciudadano():
    driver.implicitly_wait(50)
    boton_encuesta_actualizacion = mf.obtener_elemento_por_id(driver, "rl_encuesta")
    boton_encuesta_actualizacion.click()
    mf.dar_click_en_seccion_actualizacion(driver, "Sección 4292")
    mf.dar_click_en_ciudadano(driver, "PUCH CASTRO LUIS ELEAZAR")
    mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
    mf.siguiente(driver)


def test_uso_de_domicilio():
    opcion2_1 = mf.obtener_elemento_radiobutton_xpath(driver, "Vivienda")
    opcion2_1.click()
    pregunta2_2 = mf.obtener_elemento_text_view_xpath(driver, "2.1. ¿QUÉ USO TIENE EL DOMICILIO?")
    assert pregunta2_2.is_displayed()
    opcion2_2_1 = mf.obtener_elemento_radiobutton_xpath(driver, "Si")
    opcion2_2_1.click()
    mf.siguiente(driver)




def test_realizacion_de_la_entrevista():
    pregunta3 = mf.obtener_elemento_text_view_xpath(driver, "3. Realización de la entrevista.")
    assert pregunta3.is_displayed()
    opcion3_1_1 = mf.obtener_elemento_radiobutton_xpath(driver, "No, por ausencia")
    opcion3_1_1.click()
    driver.swipe(520, 1914, 520, 1047)
    agendar = mf.obtener_elemento_text_view_xpath(driver, "¿AGENDAR UNA SIGUIENTE VISITA?")
    assert agendar.is_displayed()
    opcion3_1_2 = mf.obtener_elemento_radiobutton_xpath(driver, "No")
    opcion3_1_2.click()
    driver.swipe(520, 1914, 520, 1047)
    causa=mf.obtener_elemento_por_id(driver, "causaEdit")
    causa.set_text("No se agenda por ausencia")
    boton_finalizar_encuesta= mf.obtener_elemento_por_id(driver, "finalizar_encuesta")
    boton_finalizar_encuesta.click()

def test_envio_cedulas():
    mf.enviar_cedulas(driver)
    time.sleep(10)
    driver.quit()



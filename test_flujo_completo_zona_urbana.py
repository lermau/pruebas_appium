import gc
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import misFunciones as mf
import funcionesApp as funApp
import time

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
driver.implicitly_wait(30)


# @pytest.mark.skip()
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
    textoUsuario.send_keys("EN010103")
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


# Acceder al apartado de cobertura
def test_conteo_cobertura():
    boton_encuesta_cobertura = driver.find_element(AppiumBy.ID, 'com.ine.app:id/rl_cobertura')
    boton_encuesta_cobertura.click()
    wait = WebDriverWait(driver, 10)
    # Esperar a que el título "Conteo de Viviendas" aparezca
    titulo_conteo_de_viviendas = wait.until(
        EC.text_to_be_present_in_element((AppiumBy.ID, 'com.ine.app:id/title'), "Conteo de Viviendas"))
    assert titulo_conteo_de_viviendas


@pytest.mark.skip()
def test_click_seccion():
    # mf.dar_click_seccion(driver, "Seccion 362")
    seccion = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/card_layout')
    seccion[1].click()


# @pytest.mark.skip()
def test_click_manzana_69():
    """"Guardar los 5 registros del portal seleccionarlos y enviarlos """
    mf.dar_click_seccion(driver, "Sección 362")
    mf.dar_click_en_manzana_con_numero(driver, "Manzana 69")
    mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
    mf.click_a_calle(driver, "RIOS")
    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_click_manzana_49():
    """Poner solo 2 viviendas habitadas"""
    mf.dar_click_tab_en_proceso(driver)
    mf.dar_click_seccion(driver, "Sección 362")
    mf.dar_click_en_manzana_con_numero(driver, "Manzana 49")
    mf.click_a_calle(driver, "CAFE")

    wait = WebDriverWait(driver, 10)
    opciones_no = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
    print(len(opciones_no))

    opciones_no[1].click()
    opciones_no[5].click()
    opciones_no[9].click()

    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_click_manzana_75():
    """Conteo de manzana a la que se le agregan 5 direcciones nuevas y se ponen las que vienen del portal como
       deshabitadas"""
    mf.dar_click_tab_en_proceso(driver)
    mf.dar_click_seccion(driver, "Sección 362")

    mf.dar_click_en_manzana_con_numero(driver, "Manzana 75")
    mf.click_a_calle(driver, "ABEJITAS")

    wait = WebDriverWait(driver, 10)
    opciones_no = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
    print(len(opciones_no))
    for no in range(1, 11, 2):
        opciones_no[no].click()
        time.sleep(.5)

    numero_exterior = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/numExtEdit")))
    for num in range(1, 6):
        numero_exterior.send_keys(num * 10)
        # time.sleep(.5)
        driver.swipe(520, 1914, 520, 1047)
        agregar_registros = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/agregar")))
        agregar_registros.click()
        numero_exterior.clear()

    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_click_manzana_78():
    """Se ponen todas las viviendas que vienen del portal como deshabitadas"""
    mf.dar_click_tab_en_proceso(driver)
    mf.dar_click_seccion(driver, "Sección 362")

    mf.dar_click_en_manzana_con_numero(driver, "Manzana 78")
    mf.click_a_calle(driver, "DURAZNOS")

    wait = WebDriverWait(driver, 10)
    opciones_no = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
    print(len(opciones_no))
    for no in range(1, 11, 2):
        opciones_no[no].click()
        time.sleep(.5)

    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_click_manzana_96():
    """Se agregan 5 registros con el número exterior 1 """
    mf.dar_click_tab_en_proceso(driver)
    mf.dar_click_seccion(driver, "Sección 362")

    mf.dar_click_en_manzana_con_numero(driver, "Manzana 96")
    mf.click_a_calle(driver, "LIMAS")

    wait = WebDriverWait(driver, 10)
    numero_exterior = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/numExtEdit")))
    for num in range(1, 6):
        numero_exterior.send_keys(1)
        # time.sleep(.5)
        driver.swipe(520, 1914, 520, 1047)
        agregar_registros = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/agregar")))
        agregar_registros.click()
        numero_exterior.clear()

    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_click_manzana_104():
    """Se ponen todas las viviendas que vienen del portal como deshabitadas"""
    mf.dar_click_tab_en_proceso(driver)
    mf.dar_click_seccion(driver, "Sección 362")

    mf.dar_click_en_manzana_con_numero(driver, "Manzana 104")
    mf.click_a_calle(driver, "LIMAS")

    wait = WebDriverWait(driver, 10)
    opciones_no = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
    print(len(opciones_no))
    for no in range(1, 11, 2):
        opciones_no[no].click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_exterior = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/numExtEdit")))
    for num in range(1, 6):
        numero_exterior.send_keys(1)
        # time.sleep(.5)
        driver.swipe(520, 1914, 520, 1047)
        agregar_registros = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/agregar")))
        agregar_registros.click()
        numero_exterior.clear()

    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_click_manzana_8():
    """"Guardar los 5 registros del portal seleccionarlos y enviarlos """
    mf.dar_click_seccion(driver, "Sección 384")
    mf.dar_click_en_manzana_con_numero(driver, "Manzana 8")
    # mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
    mf.click_a_calle(driver, "CAFE")
    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_click_manzana_14():
    """"Guardar los 5 registros del portal seleccionarlos y enviarlos """
    mf.dar_click_seccion(driver, "Sección 384")
    mf.dar_click_en_manzana_con_numero(driver, "Manzana 14")
    # comentar cuando sena la prueba completa
    # mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
    mf.click_a_calle(driver, "RIOS")
    wait = WebDriverWait(driver, 10)
    viviendas_interiores = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.EditText")))

    for no in range(0, 5):
        viviendas_interiores[no].clear()
        viviendas_interiores[no].send_keys("5")
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)


# @pytest.mark.skip()
def test_envio_seleccion():
    """"Hacer la selección y envío de las secciones """
    mf.dar_click_en_seleccionar(driver)


#     mf.dar_click_en_enviar_seleccion(driver)
def test_HP():
    funApp.happy_path_urbana(driver)

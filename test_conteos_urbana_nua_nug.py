import gc
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import misFunciones as mf
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


# @pytest.mark.skip()
# def test_click_seccion():
#     #mf.dar_click_seccion(driver, "Seccion 362")
#     seccion = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/card_layout')
#     seccion[1].click()
#
#
# #@pytest.mark.skip()
# def test_click_manzana_69():
#     """"Guardar los 5 registros del portal seleccionarlos y enviarlos """
#     mf.dar_click_seccion(driver, "Sección 362")
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 69")
#     mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
#     mf.click_a_calle(driver, "RIOS")
#     mf.guardar_registros_conteo(driver)
#
#
# #@pytest.mark.skip()
# def test_click_manzana_49():
#     """Poner solo 2 viviendas habitadas"""
#     mf.dar_click_tab_en_proceso(driver)
#     mf.dar_click_seccion(driver, "Sección 362")
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 49")
#     mf.click_a_calle(driver, "CAFE")
#
#     wait = WebDriverWait(driver, 10)
#     opciones_no = wait.until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
#     print(len(opciones_no))
#
#     opciones_no[1].click()
#     opciones_no[5].click()
#     opciones_no[9].click()
#
#     mf.guardar_registros_conteo(driver)
#
#
# #@pytest.mark.skip()
# def test_click_manzana_75():
#     """Conteo de manzana a la que se le agregan 5 direcciones nuevas y se ponen las que vienen del portal como
#        deshabitadas"""
#     mf.dar_click_tab_en_proceso(driver)
#     mf.dar_click_seccion(driver, "Sección 362")
#
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 75")
#     mf.click_a_calle(driver, "ABEJITAS")
#
#     wait = WebDriverWait(driver, 10)
#     opciones_no = wait.until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
#     print(len(opciones_no))
#     for no in range(1, 11, 2):
#         opciones_no[no].click()
#         time.sleep(.5)
#
#     numero_exterior = wait.until(
#         EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/numExtEdit")))
#     for num in range(1, 6):
#         numero_exterior.send_keys(num * 10)
#         # time.sleep(.5)
#         driver.swipe(520, 1914, 520, 1047)
#         agregar_registros = wait.until(
#             EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/agregar")))
#         agregar_registros.click()
#         numero_exterior.clear()
#
#     mf.guardar_registros_conteo(driver)
#
#
# #@pytest.mark.skip()
# def test_click_manzana_78():
#     """Se ponen todas las viviendas que vienen del portal como deshabitadas"""
#     mf.dar_click_tab_en_proceso(driver)
#     mf.dar_click_seccion(driver, "Sección 362")
#
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 78")
#     mf.click_a_calle(driver, "DURAZNOS")
#
#     wait = WebDriverWait(driver, 10)
#     opciones_no = wait.until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
#     print(len(opciones_no))
#     for no in range(1, 11, 2):
#         opciones_no[no].click()
#         time.sleep(.5)
#
#     mf.guardar_registros_conteo(driver)
#
#
# #@pytest.mark.skip()
# def test_click_manzana_96():
#     """Se agregan 5 registros con el número exterior 1 """
#     mf.dar_click_tab_en_proceso(driver)
#     mf.dar_click_seccion(driver, "Sección 362")
#
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 96")
#     mf.click_a_calle(driver, "LIMAS")
#
#     wait = WebDriverWait(driver, 10)
#     numero_exterior = wait.until(
#         EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/numExtEdit")))
#     for num in range(1, 6):
#         numero_exterior.send_keys(1)
#         # time.sleep(.5)
#         driver.swipe(520, 1914, 520, 1047)
#         agregar_registros = wait.until(
#             EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/agregar")))
#         agregar_registros.click()
#         numero_exterior.clear()
#
#     mf.guardar_registros_conteo(driver)
#
#
# #@pytest.mark.skip()
# def test_click_manzana_104():
#     """Se ponen todas las viviendas que vienen del portal como deshabitadas"""
#     mf.dar_click_tab_en_proceso(driver)
#     mf.dar_click_seccion(driver, "Sección 362")
#
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 104")
#     mf.click_a_calle(driver, "LIMAS")
#
#     wait = WebDriverWait(driver, 10)
#     opciones_no = wait.until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RadioButton")))
#     print(len(opciones_no))
#     for no in range(1, 11, 2):
#         opciones_no[no].click()
#         time.sleep(.5)
#
#     wait = WebDriverWait(driver, 10)
#     numero_exterior = wait.until(
#         EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/numExtEdit")))
#     for num in range(1, 6):
#         numero_exterior.send_keys(1)
#         # time.sleep(.5)
#         driver.swipe(520, 1914, 520, 1047)
#         agregar_registros = wait.until(
#             EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/agregar")))
#         agregar_registros.click()
#         numero_exterior.clear()
#
#     mf.guardar_registros_conteo(driver)
#
#
# #@pytest.mark.skip()
# def test_click_manzana_8():
#     """"Guardar los 5 registros del portal seleccionarlos y enviarlos """
#     mf.dar_click_seccion(driver, "Sección 384")
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 8")
#     # mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
#     mf.click_a_calle(driver, "CAFE")
#     mf.guardar_registros_conteo(driver)
#
# #@pytest.mark.skip()
# def test_click_manzana_14():
#     """"Guardar los 5 registros del portal seleccionarlos y enviarlos """
#     mf.dar_click_seccion(driver, "Sección 384")
#     mf.dar_click_en_manzana_con_numero(driver, "Manzana 14")
#     #comentar cuando sena la prueba completa
#     #mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
#     mf.click_a_calle(driver, "RIOS")
#     wait = WebDriverWait(driver, 10)
#     viviendas_interiores = wait.until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.EditText")))
#
#     for no in range(0,5):
#         viviendas_interiores[no].clear()
#         viviendas_interiores[no].send_keys("5")
#         time.sleep(.5)
#     mf.guardar_registros_conteo(driver)
#
#
#
# @pytest.mark.skip()
# def test_envío_seleccion():
#     """"Guardar los 5 registros del portal seleccionarlos y enviarlos """
#     mf.dar_click_en_seleccionar(driver)
#     mf.dar_click_en_enviar_seleccion(driver)

#######CONTEO ZONA NO URBANA GENERAL################################

# # @pytest.mark.skip()
# def test_zona_NUG_localidad_11():
#     """Se ponen agregan 6 localidades y se envian las 6"""
#     mf.dar_click_en_tab_zona(driver, "NO URBANA GENERAL")
#     mf.dar_click_localidad(driver, "Localidad 11")
#     mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
#     boton_agregar_registros = driver.find_element(AppiumBy.ID, 'com.ine.app:id/agregarRegistros')
#     for x in range(5):
#         boton_agregar_registros.click()
#     numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
#     num = 1
#     for x in numero_campos:
#         x.set_text(f"Localidad 11 Distrito 1 Seccion 427 vivienda {num}")
#         num += 1
#     mf.guardar_registros_conteo(driver)
#
#
# # @pytest.mark.skip()
# def test_zona_NUG_localidad_15():
#     """Se ponen agregan 3 localidades y se envian todas"""
#     mf.dar_click_en_tab_zona(driver, "NO URBANA GENERAL")
#     mf.dar_click_localidad(driver, "Localidad 15")
#     # mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
#     boton_agregar_registros = driver.find_element(AppiumBy.ID, 'com.ine.app:id/agregarRegistros')
#     for x in range(2):
#         boton_agregar_registros.click()
#     numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
#     num = 1
#     for x in numero_campos:
#         x.set_text(f"Localidad 15 Distrito 1 Seccion 427 vivienda {num}")
#         num += 1
#     mf.guardar_registros_conteo(driver)


# def test_zona_NUG_localidad_65():
#     """Se ponen agregan 8 localidades y se envian las 6 que se seleccionan"""
#     mf.dar_click_en_tab_zona(driver, "NO URBANA GENERAL")
#     mf.dar_click_localidad(driver, "Localidad 65")
#     mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
#     boton_agregar_registros = driver.find_element(AppiumBy.ID, 'com.ine.app:id/agregarRegistros')
#     for x in range(6):
#         boton_agregar_registros.click()
#     numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
#
#     num = 1
#     for x in numero_campos:
#         driver.swipe(520, 1514, 520, 1047)
#         x.set_text(f"Localidad 65 Distrito 1 Seccion 427 vivienda {num}")
#         num += 1
#     mf.guardar_registros_conteo(driver)



# def test_zona_NUG_localidad_76():
#     """Se elimina esta carga desde el portal para que no llegue la información"""
#     mf.dar_click_en_tab_zona(driver, "NO URBANA GENERAL")
#     mf.dar_click_localidad(driver, "Localidad 76")
#     mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
#     boton_agregar_registros = driver.find_element(AppiumBy.ID, 'com.ine.app:id/agregarRegistros')
#     for x in range(6):
#         boton_agregar_registros.click()
#         time.sleep(.5)
#     numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
#     print(len(numero_campos))
#     driver.swipe(520, 1600, 520, 850)
#     num = 1
#     # for x in numero_campos:
#     #     driver.swipe(520, 1600, 520, 950)
#     #     x.set_text(f"Localidad 76 Distrito 1 Seccion 427 vivienda {num}")
#     #     num += 1
#
#     for x in range(len(numero_campos)):
#         numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
#         driver.swipe(520, 1600, 520, 950)
#         numero_campos[x].set_text(f"Localidad 76 Distrito 1 Seccion 427 vivienda {num}")
#         num += 1
#         driver.swipe(520, 1600, 520, 950)
#         time.sleep(.5)
#     mf.guardar_registros_conteo(driver)
################################################################################
######################ZONA NO URBANA AlTERNA####################################
################################################################################
def test_zona_NUG_pseudomanzanas_localidad_22():
    """Se agregan solo 2 pseudomanzanas"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 22")
    mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
    boton_agregar_registros = driver.find_element(AppiumBy.ID, 'com.ine.app:id/agregarRegistros')
    for x in range(1):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Localidad 22 Distrito 1 Seccion 343 pseudomanzana {num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_viviendas_pseudomanzana_1_localidad_22():
    """agregado de 3 viviendas pseudomanzana1"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 22")
    mf.dar_click_pseudomanzana(driver, 0)
    wait = WebDriverWait(driver, 10)
    boton_agregar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/agregarRegistros')))

    for x in range(2):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Pseudomanzana 1 vivienda{num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_viviendas_pseudomanzana_2_localidad_22():
    """agregado de 3 viviendas pseudomanzana2 """
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 22")
    mf.dar_click_pseudomanzana(driver, 0)
    wait = WebDriverWait(driver, 10)
    boton_agregar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/agregarRegistros')))

    for x in range(2):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Pseudomanzana 2 vivienda{num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_pseudomanzanas_localidad_42():
    """Se agregan 5 pseudomanzanas"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 42")
    #mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
    boton_agregar_registros = driver.find_element(AppiumBy.ID, 'com.ine.app:id/agregarRegistros')
    for x in range(4):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Localidad 42 Distrito 1 Seccion 374 pseudomanzana {num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_viviendas_pseudomanzana_1_localidad_42():
    """agregado de 5 viviendas pseudomanzana1"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 42")
    mf.dar_click_pseudomanzana(driver, 0)
    wait = WebDriverWait(driver, 10)
    boton_agregar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/agregarRegistros')))

    for x in range(4):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Pseudomanzana 1 vivienda{num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_viviendas_pseudomanzana_2_localidad_42():
    """agregado de 2 viviendas pseudomanzana 2"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 42")
    mf.dar_click_pseudomanzana(driver, 0)
    wait = WebDriverWait(driver, 10)
    boton_agregar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/agregarRegistros')))

    for x in range(1):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Pseudomanzana 3 vivienda{num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

# @pytest.mark.skip()
def test_zona_NUG_pseudomanzanas_localidad_89():
    """Solo se agrega una pseudomanzana"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 89")
    numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
    numero_campos[0].set_text(f"Localidad 89 Distrito 1 Seccion 478 pseudomanzana 1")
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_viviendas_pseudomanzana_1_localidad_89():
    """agregado de 5 viviendas pseudomanzana1"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 89")
    mf.dar_click_pseudomanzana(driver, 0)
    wait = WebDriverWait(driver, 10)
    boton_agregar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/agregarRegistros')))

    for x in range(4):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Pseudomanzana 1 vivienda{num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_pseudomanzanas_localidad_72():
    """Se agregan solo 2 pseudomanzanas"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 72")
    #mf.dar_click_en_aceptar_usu_de_coordenadas(driver)
    boton_agregar_registros = driver.find_element(AppiumBy.ID, 'com.ine.app:id/agregarRegistros')
    for x in range(2):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Localidad 72 Distrito 1 Seccion 442 pseudomanzana {num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_viviendas_pseudomanzana_1_localidad_72():
    """agregado de 5 viviendas pseudomanzana1 se elimina antes de enviar"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 72")
    mf.dar_click_pseudomanzana(driver, 0)
    wait = WebDriverWait(driver, 10)
    boton_agregar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/agregarRegistros')))

    for x in range(4):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Pseudomanzana 1 vivienda{num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)

def test_zona_NUG_viviendas_pseudomanzana_2_localidad_72():
    """agregado de 5 viviendas pseudomanzana2 se elimina antes de enviar"""
    mf.dar_click_en_tab_zona(driver, "NO URBANA ALTERNO")
    mf.dar_click_localidad(driver, "Localidad 72")
    mf.dar_click_pseudomanzana(driver, 0)
    wait = WebDriverWait(driver, 10)
    boton_agregar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/agregarRegistros')))

    for x in range(4):
        boton_agregar_registros.click()
        time.sleep(.5)

    wait = WebDriverWait(driver, 10)
    numero_campos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/editCaracteristicas")))
    print(len(numero_campos))
    driver.swipe(520, 1600, 520, 850)
    num = 1

    for x in range(len(numero_campos)):
        numero_campos = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/editCaracteristicas')
        driver.swipe(520, 1600, 520, 950)
        numero_campos[x].set_text(f"Pseudomanzana 1 vivienda{num}")
        num += 1
        driver.swipe(520, 1600, 520, 950)
        time.sleep(.5)
    mf.guardar_registros_conteo(driver)




gc.collect()
time.sleep(1)

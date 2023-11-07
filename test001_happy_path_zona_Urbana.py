import gc
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import misFunciones as mf
import funcionesApp as funApp
import time
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
# print("Iniciando Test03  con Appium")
# driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
# driver.implicitly_wait(30)


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

    # texto_contrasenia.click()
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


def test_menu_lateral_y_apartado_viviendas_seleccionadas():
    boton_avatar = mf.obtener_elemento_por_id(driver, "avatar")
    boton_avatar.click()
    clave_usuario = driver.find_element(AppiumBy.ID, "com.ine.app:id/userName")
    assert clave_usuario.text == "EN010103"
    nombre_usuario = driver.find_element(AppiumBy.ID, "com.ine.app:id/userFullName")
    # assert nombre_usuario.text == "MAURICIO VALERMA VALERMA"
    submenu_cobertura = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Cobertura']")
    submenu_cobertura.click()
    opcion_viviendas_seleccionadas = driver.find_element(AppiumBy.XPATH,
                                                         "//android.widget.TextView[@text='Viviendas seleccionadas']")
    opcion_viviendas_seleccionadas.click()


def test_click_manzana_69():
    """"""
    mf.dar_click_tab_en_proceso(driver)
    mf.dar_click_en_manzana_seleccionada(driver, "Manzana 69, Sección 362")


def test_click_manzana_69_vivienda1():
    """se selecciona la vivienda 1 de la manzana 8 para iniciar encuestas"""
    # mf.dar_click_tab_en_proceso(driver)
    mf.dar_click_en_vivienda_de_manzana_seleccionada(driver, "Vivienda 1")

    vivienda_card = mf.obtener_elemento_por_id(driver, "text_vivienda")
    assert "Vivienda 01" == vivienda_card.text
    seccion_card = mf.obtener_elemento_por_id(driver, "text_seccion")
    assert "SECCIÓN: 362" == seccion_card.text
    manzana_card = mf.obtener_elemento_por_id(driver, "text_manzana")
    assert "MANZANA: 69" == manzana_card.text
    distrito_card = mf.obtener_elemento_por_id(driver, "text_distrito")
    assert "DISTRITO: 01" == distrito_card.text

    boton_seleccionar_en_card = driver.find_element(AppiumBy.ID, "com.ine.app:id/btn_seleccionar")
    boton_seleccionar_en_card.click()
    mf.dar_click_en_aceptar_usu_de_coordenadas(driver)


def test_validar_informacion_Geoelectoral():
    """Test para comprobar la informacion geoelectoral pregunta 1"""
    texto_entidad = mf.obtener_elemento_por_id(driver, "entidad")
    assert "Entidad: Aguascalientes" == texto_entidad.text
    texto_distrito = mf.obtener_elemento_por_id(driver, "distrito")
    assert "Distrito: 1" == texto_distrito.text
    texto_municipio = mf.obtener_elemento_por_id(driver, "municipio")
    assert "Municipio: CALVILLO" == texto_municipio.text
    texto_seccion = mf.obtener_elemento_por_id(driver, "seccion")
    assert "Sección: 362" == texto_seccion.text
    texto_localidad = mf.obtener_elemento_por_id(driver, "localidad")
    assert "Localidad: CALVILLO" == texto_localidad.text
    texto_manzana = mf.obtener_elemento_por_id(driver, "manzana")
    assert "Manzana: 69" == texto_manzana.text


def test_validar_informacion_Domicilio():
    """Test para comprobar la informacion geoelectoral pregunta 1"""
    texto_calle = mf.obtener_elemento_por_id(driver, "calle")
    assert "Calle: RIOS" == texto_calle.text
    texto_numExterior = mf.obtener_elemento_por_id(driver, "numExterior")
    assert "Número exterior: 1" == texto_numExterior.text
    texto_colonia_localidad = mf.obtener_elemento_por_id(driver, "coloniaLocalidad")
    assert "Colonia o Localidad: CALVILLO" == texto_colonia_localidad.text
    texto_consecutivo = mf.obtener_elemento_por_id(driver, "consecutivo")
    assert "Consecutivo de vivienda: 1" == texto_consecutivo.text


def test_cuestionario_pregunta_3():
    """Se contesta la pregunta 3 con la opción 1 vivienda habitada"""
    mf.siguiente(driver)
    pregunta3 = mf.obtener_lista_de_elementos_id(driver, "opcion")
    pregunta3[0].click()
    mf.siguiente(driver)


def test_cuestionario_pregunta_4():
    """Se contesta la pregunta 3 con la opción 1 vivienda habitada"""
    pregunta4 = mf.obtener_lista_de_elementos_radiobutom(driver)
    pregunta4[0].click()
    mf.siguiente(driver)


def test_cuestionario_pregunta_5_2():
    """Se contesta la pregunta 3 con la opción 1 vivienda habitada"""
    pregunta5_2 = mf.obtener_elemento_por_id(
        driver, "encuesta_cobertura_seccion_5_edittext_personas_18_o_mas")
    pregunta5_2.click()
    pregunta5_2.set_text("1")
    driver.hide_keyboard()
    mf.siguiente(driver)


def test_agregar_habitante():
    funApp.agregar_ciudadano_fuera_del_padron(driver, "Valencia", "Lerma", "Mauricio")
    ciudadano1 = mf.obtener_lista_de_elementos_id(driver, "nombreTextView")
    ciudadano1[0].click()
    funApp.seleccionar_fecha_nacimiento(driver, "1921", mf.fecha_de_nacimiento())
    sexo = mf.obtener_elemento_radiobutton_xpath(driver, "Hombre")
    sexo.click()
    driver.swipe(520, 1914, 520, 1047)
    grado_escolar = mf.obtener_elemento_radiobutton_xpath(driver, "Ninguno")
    grado_escolar.click()
    driver.swipe(520, 1914, 520, 1047)
    ocupacion = mf.obtener_elemento_radiobutton_xpath(driver, "Trabaja")
    ocupacion.click()
    mf.siguiente(driver)

def test_pregunta_7_1():
    respuesta1 = mf.obtener_elemento_radiobutton_xpath(driver, "Si")
    respuesta1.click()
    mf.siguiente(driver)

def test_pregunta_9_1():
    respuesta3 = mf.obtener_elemento_radiobutton_xpath(driver, "No sabe")
    respuesta3.click()
    mf.siguiente(driver)

def test_pregunta_10_1():
    respuesta3 = mf.obtener_elemento_radiobutton_xpath(driver, "No sabe")
    respuesta3.click()
    mf.siguiente(driver)

def test_pregunta_11_1():
    respuesta1 = mf.obtener_elemento_radiobutton_xpath(driver, "Ciudadano en cuestión")
    respuesta1.click()
    boton_finalizar_encuesta = mf.obtener_elemento_por_id(driver, "finalizar")
    boton_finalizar_encuesta.click()

def test_envio_encuestas():
    mf.enviar_encuestas(driver)
    time.sleep(10)
    driver.quit()






gc.collect()
time.sleep(1)

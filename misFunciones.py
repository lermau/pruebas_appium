import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as AppiumBy
import datetime

def dar_click_seccion(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")))
    element.click()
    time.sleep(.5)


def click_a_calle(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")))
    element.click()
    time.sleep(.5)


def guardar_registros_conteo(driver):
    wait = WebDriverWait(driver, 10)
    guardar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/guardarRegistros")))
    guardar_registros.click()

    wait = WebDriverWait(driver, 10)
    confirmar_guardar_registros = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='OK']")))
    confirmar_guardar_registros.click()


def dar_click_en_seleccionar(driver):
    wait = WebDriverWait(driver, 10)
    tab_completadas_urbana = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "COMPLETADAS")))
    tab_completadas_urbana.click()

    boton_seleccionar = driver.find_element(AppiumBy.ID, "com.ine.app:id/seleccionar")
    boton_seleccionar.click()


def dar_click_en_enviar_seleccion(driver):
    wait = WebDriverWait(driver, 10)
    boton_enviar_seleccion = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.ine.app:id/enviar')))
    boton_enviar_seleccion.click()


def dar_click_en_aceptar_usu_de_coordenadas(driver):
    wait = WebDriverWait(driver, 10)
    aceptar_registro_de_coordenadas = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='ACEPTAR']")))
    aceptar_registro_de_coordenadas.click()
    time.sleep(.5)


def dar_click_en_manzana_con_numero(driver, numero_de_manzana):
    manzanas = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/childTitle')
    nombres_de_manzanas = []
    for manzana in manzanas:
        nombres_de_manzanas.append(manzana.text)
    indice_manzana = nombres_de_manzanas.index(f"{numero_de_manzana}")
    manzanas[indice_manzana].click()
    time.sleep(.5)


def dar_click_tab_en_proceso(driver):
    wait = WebDriverWait(driver, 10)
    tab_completadas_urbana = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "EN PROCESO")))
    tab_completadas_urbana.click()


def dar_click_en_tab_zona(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")))
    element.click()
    time.sleep(.5)


def dar_click_localidad(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")))
    element.click()
    time.sleep(.5)


def dar_click_boton_agregar(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")))
    element.click()
    time.sleep(.5)


def dar_click_pseudomanzana(driver, indice):
    wait = WebDriverWait(driver, 10)
    pseudomanzanas = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/childTitle")))
    pseudomanzanas[indice].click()
    time.sleep(1)


def dar_click_en_manzana_seleccionada(driver, numero_de_manzana):
    manzanas = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/parentTitle')
    nombres_de_manzanas = []
    for manzana in manzanas:
        nombres_de_manzanas.append(manzana.text)
    indice_manzana = nombres_de_manzanas.index(f"{numero_de_manzana}")
    manzanas[indice_manzana].click()
    time.sleep(.5)


def dar_click_en_vivienda_de_manzana_seleccionada(driver, numero_de_vivienda):
    viviendas = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/childTitle')
    nombres_de_viviendas = []
    for vivienda in viviendas:
        nombres_de_viviendas.append(vivienda.text)
    indice_vivienda = nombres_de_viviendas.index(f"{numero_de_vivienda}")
    viviendas[indice_vivienda].click()
    time.sleep(.5)


def dar_click_en_vivienda_de_localidad_seleccionada(driver, numero_de_vivienda):
    viviendas = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/childTitle')
    nombres_de_viviendas = []
    for vivienda in viviendas:
        nombres_de_viviendas.append(vivienda.text)
    indice_vivienda = nombres_de_viviendas.index(f"{numero_de_vivienda}")
    viviendas[indice_vivienda].click()
    time.sleep(.5)


def obtener_elemento_por_id(driver, id_nombre):
    wait = WebDriverWait(driver, 10)
    elemento = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, f"com.ine.app:id/{id_nombre}")))
    return elemento


def obtener_lista_de_elementos_id(driver, id_nombre):
    wait = WebDriverWait(driver, 10)
    lista_elementos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, f"com.ine.app:id/{id_nombre}")))
    return lista_elementos


def obtener_lista_de_elementos_radiobutom(driver):
    wait = WebDriverWait(driver, 10)
    lista_elementos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.CLASS_NAME, "android.widget.RadioButton")))
    return lista_elementos


def obtener_lista_de_elementos_textview(driver, nombre):
    wait = WebDriverWait(driver, 10)
    lista_elementos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{nombre}']")))
    return lista_elementos


def siguiente(driver):
    boton_siguiente = driver.find_element(AppiumBy.ID, "com.ine.app:id/siguiente")
    click_boton_siguiente = boton_siguiente
    click_boton_siguiente.click()
    time.sleep(.5)


def siguiente_atras(driver, AppiumBy):
    boton_siguiente = driver.find_element(AppiumBy.ID, "com.ine.app:id/siguiente")
    click_boton_siguiente = boton_siguiente
    click_boton_siguiente.click()
    boton_atras = driver.find_element(AppiumBy.ID, "com.ine.app:id/anterior")
    click_boton_atras = boton_atras
    click_boton_atras.click()
    time.sleep(.5)


def atras(driver, AppiumBy):
    boton_atras = driver.find_element(AppiumBy.ID, "com.ine.app:id/anterior")
    click_boton_atras = boton_atras
    click_boton_atras.click()
    time.sleep(.5)


def obtener_elemento_radiobutton_xpath(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.RadioButton[@text='{text}']")))
    return element


def obtener_elemento_text_view_xpath(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")))
    return element

def obtener_elemento_CheckedTextview_xpath(driver, text):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.CheckedTextView[@text='{text}']")))
    return element


def enviar_encuestas(driver):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='COMPLETADAS']")))
    element.click()
    boton_enviar_encuesta = obtener_elemento_por_id(driver, "enviar")
    boton_enviar_encuesta.click()


def enviar_cedulas(driver):
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='COMPLETADAS']")))
    element.click()
    boton_enviar_cedula = obtener_elemento_por_id(driver, "proceder")
    boton_enviar_cedula.click()



def dar_click_en_localidad_seleccionada(driver, nombre_localidad):
    localidades = driver.find_elements(AppiumBy.ID, 'com.ine.app:id/parentTitle')
    nombres_de_localidades = []
    for localidad in localidades:
        nombres_de_localidades.append(localidad.text)
    indice_localidad = nombres_de_localidades.index(f"{nombre_localidad}")
    localidades[indice_localidad].click()
    time.sleep(.5)


def dar_click_en_seccion_actualizacion(driver, nombre_ciudadano):
    wait = WebDriverWait(driver, 10)
    lista_secciones = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/parentTitle")))
    #lista_secciones[0].click()
    numeros_de_seccion = []
    for seccion in lista_secciones:
        numeros_de_seccion.append(seccion.text)
    indice_seccion = numeros_de_seccion.index(f"{nombre_ciudadano}")
    lista_secciones[indice_seccion].click()
    time.sleep(.5)


def dar_click_en_ciudadano(driver, nombre_ciudadano):
    wait = WebDriverWait(driver, 10)
    lista_ciudadanos = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "com.ine.app:id/childTitle")))
    #lista_secciones[0].click()
    print(len(lista_ciudadanos))
    nombres_de_ciudadanos = []
    for ciudadano in lista_ciudadanos:
        nombres_de_ciudadanos.append(ciudadano.text)
    indice_ciudadano = nombres_de_ciudadanos.index(f"{nombre_ciudadano}")
    lista_ciudadanos[indice_ciudadano].click()
    time.sleep(.5)





def fecha_de_nacimiento():
    # Obtén la fecha actual
    fecha_actual = datetime.date.today()
    # Obtiene el mes de la fecha actual como un número entero (1 para enero, 2 para febrero, etc.)
    mes_actual = fecha_actual.month
    dias_de_la_semana = ("lun.", "mar.", "mié.", "jue.", "vie.", "sáb.", "dom.")
    mes = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre",
    "diciembre")
    fechaNacimiento = datetime.date(1921, mes_actual, 9)
    fechaArmada = f"{dias_de_la_semana[fechaNacimiento.weekday()]}, 9 de {mes[mes_actual - 1]} de 1921"
    # print(fechaArmada)
    return fechaArmada
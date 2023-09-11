import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as AppiumBy


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


def obtener_elemento_por_id(driver, id_nombre):
    wait = WebDriverWait(driver, 10)
    elemento = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, f"com.ine.app:id/{id_nombre}")))
    return elemento

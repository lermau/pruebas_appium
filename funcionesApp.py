import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as AppiumBy
import misFunciones as mf


def agregar_ciudadano_fuera_del_padron(driver, apellidoPaterno, apellidoMaterno, nombre):
    busqueda_padron = mf.obtener_elemento_text_view_xpath(driver, "Bùsqueda en padrón")
    busqueda_padron.click()
    sin_coincidencia = mf.obtener_elemento_text_view_xpath(driver, "Selecciona aquí si no hay coincidencias")
    sin_coincidencia.click()
    apellido_paterno = mf.obtener_elemento_por_id(driver, "apellidoPaternoEditText")
    apellido_paterno.send_keys(apellidoPaterno)
    apellido_materno = mf.obtener_elemento_por_id(driver, "apellidoMaternoEditText")
    apellido_materno.send_keys(apellidoMaterno)
    nombres = mf.obtener_elemento_por_id(driver, "nombresEditText")
    nombres.send_keys(nombre)
    boton_registrar_habitante = mf.obtener_elemento_por_id(driver, "btn_registrar")
    boton_registrar_habitante.click()


def seleccionar_fecha_nacimiento(driver, ano, dia):
    fecha = mf.obtener_elemento_por_id(driver, "fecha")
    fecha.click()
    anio = driver.find_element(AppiumBy.ID, "com.ine.app:id/month_navigation_fragment_toggle")
    click_anio = anio
    click_anio.click()
    driver.swipe(520, 747, 520, 1914)
    time.sleep(1)
    driver.swipe(520, 747, 520, 1914)
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    anio_selec = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"Navegar al año {ano}")))
    anio_selec.click()
    time.sleep(3)
    dia_selec = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"{dia}")))
    time.sleep(2)
    dia_selec.click()
    boton_confirmar = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.ine.app:id/confirm_button")))
    boton_confirmar.click()

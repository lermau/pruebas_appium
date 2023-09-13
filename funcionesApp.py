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


def happy_path_urbana(driver):
    #def test_menu_lateral_y_apartado_viviendas_seleccionadas():
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

    #def test_click_manzana_8():
        """"""
        mf.dar_click_tab_en_proceso(driver)
        mf.dar_click_en_manzana_seleccionada(driver, "Manzana 8")

    #def test_click_manzana_8_vivienda1():
        """se selecciona la vivienda 1 de la manzana 8 para iniciar encuestas"""
        # mf.dar_click_tab_en_proceso(driver)
        mf.dar_click_en_vivienda_de_manzana_seleccionada(driver, "Vivienda 1")

        vivienda_card = mf.obtener_elemento_por_id(driver, "text_vivienda")
        assert "Vivienda 01" == vivienda_card.text
        seccion_card = mf.obtener_elemento_por_id(driver, "text_seccion")
        assert "SECCION: 384" == seccion_card.text
        manzana_card = mf.obtener_elemento_por_id(driver, "text_manzana")
        assert "MANZANA: 08" == manzana_card.text
        distrito_card = mf.obtener_elemento_por_id(driver, "text_distrito")
        assert "DISTRITO: 01" == distrito_card.text

        boton_seleccionar_en_card = driver.find_element(AppiumBy.ID, "com.ine.app:id/btn_seleccionar")
        boton_seleccionar_en_card.click()
        #mf.dar_click_en_aceptar_usu_de_coordenadas(driver)

    #def test_validar_informacion_Geoelectoral():
        """Test para comprobar la informacion geoelectoral pregunta 1"""
        texto_entidad = mf.obtener_elemento_por_id(driver, "entidad")
        assert "Entidad: Aguascalientes" == texto_entidad.text
        texto_distrito = mf.obtener_elemento_por_id(driver, "distrito")
        assert "Distrito: 1" == texto_distrito.text
        texto_municipio = mf.obtener_elemento_por_id(driver, "municipio")
        assert "Municipio: CALVILLO" == texto_municipio.text
        texto_seccion = mf.obtener_elemento_por_id(driver, "seccion")
        assert "Seccion: 384" == texto_seccion.text
        texto_localidad = mf.obtener_elemento_por_id(driver, "localidad")
        assert "Localidad: CALVILLO" == texto_localidad.text
        texto_manzana = mf.obtener_elemento_por_id(driver, "manzana")
        assert "Manzana: 8" == texto_manzana.text

    #def test_validar_informacion_Domicilio():
        """Test para comprobar la informacion geoelectoral pregunta 1"""
        texto_calle = mf.obtener_elemento_por_id(driver, "calle")
        assert "Calle: CAFE" == texto_calle.text
        texto_numExterior = mf.obtener_elemento_por_id(driver, "numExterior")
        assert "Número exterior: 1" == texto_numExterior.text
        texto_colonia_localidad = mf.obtener_elemento_por_id(driver, "coloniaLocalidad")
        assert "Colonia o Localidad: CALVILLO" == texto_colonia_localidad.text
        texto_consecutivo = mf.obtener_elemento_por_id(driver, "consecutivo")
        assert "Consecutivo de vivienda: 1" == texto_consecutivo.text

    #def test_cuestionario_pregunta_3():
        """Se contesta la pregunta 3 con la opción 1 vivienda habitada"""
        mf.siguiente(driver)
        pregunta3 = mf.obtener_lista_de_elementos_id(driver, "opcion")
        pregunta3[0].click()
        mf.siguiente(driver)

    #def test_cuestionario_pregunta_4():
        """Se contesta la pregunta 3 con la opción 1 vivienda habitada"""
        pregunta4 = mf.obtener_lista_de_elementos_radiobutom(driver)
        pregunta4[0].click()
        mf.siguiente(driver)

    #def test_cuestionario_pregunta_5_2():
        """Se contesta la pregunta 3 con la opción 1 vivienda habitada"""
        pregunta5_2 = mf.obtener_elemento_por_id(
            driver, "encuesta_cobertura_seccion_5_edittext_personas_18_o_mas")
        pregunta5_2.click()
        pregunta5_2.set_text("1")
        driver.hide_keyboard()
        mf.siguiente(driver)

    #def test_agregar_habitante():
        agregar_ciudadano_fuera_del_padron(driver, "Valencia", "Lerma", "Mauricio")
        ciudadano1 = mf.obtener_lista_de_elementos_id(driver, "nombreTextView")
        ciudadano1[0].click()
        seleccionar_fecha_nacimiento(driver, "1921", "lun., 12 de septiembre de 1921")
        sexo = mf.obtener_elemento_radiobutton_xpath(driver, "Mujer")
        sexo.click()
        driver.swipe(520, 1914, 520, 1047)
        grado_escolar = mf.obtener_elemento_radiobutton_xpath(driver, "Ninguno")
        grado_escolar.click()
        driver.swipe(520, 1914, 520, 1047)
        ocupacion = mf.obtener_elemento_radiobutton_xpath(driver, "Trabaja")
        ocupacion.click()
        mf.siguiente(driver)

    #def test_pregunta_7_1():
        respuesta1 = mf.obtener_elemento_radiobutton_xpath(driver, "Si")
        respuesta1.click()
        mf.siguiente(driver)

    #def test_pregunta_9_1():
        respuesta3 = mf.obtener_elemento_radiobutton_xpath(driver, "No sabe")
        respuesta3.click()
        mf.siguiente(driver)

    #def test_pregunta_10_1():
        respuesta3 = mf.obtener_elemento_radiobutton_xpath(driver, "No sabe")
        respuesta3.click()
        mf.siguiente(driver)

    #def test_pregunta_11_1():
        respuesta1 = mf.obtener_elemento_radiobutton_xpath(driver, "Ciudadano en cuestión")
        respuesta1.click()
        boton_finalizar_encuesta = mf.obtener_elemento_por_id(driver, "finalizar")
        boton_finalizar_encuesta.click()


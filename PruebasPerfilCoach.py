
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\56949\\Downloads\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()


#Credenciales
#Admin
# user = "ne.gomezg@duocuc.cl"
# password = "Nels.9876"

#Coach
userCoach = "coachpruebaqa@gmail.com"
passwordCoach = "Dani.9999"

#Links
Link1 = "https://www.youtube.com/watch?v=b4Y6hNOQ_0o"


# #Coachee
# user = "s.ledezma@duocuc.cl"
# password = "Stef.9494"

# Inicializamos el navegador
driver.get('https://www.sistemabitacoracoaching.tk/')
#driver.get('http://127.0.0.1:8000/')

#Login al servicio 
try:
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/input').send_keys(userCoach)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/input').send_keys(passwordCoach)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
     print("Prueba realizada con exito")
except:
     print("Fallo login")


#Validación credenciales
try:
     driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #ingreso a perfil
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/a[1]').click() #busqueda de correo en perfil
     time.sleep(1)
     usuarioActual = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/input').get_attribute('value') #seleccion de correo en perfil
     time.sleep(2)
     if usuarioActual== userCoach:
          print ("Usuario correcto")
     else: 
          assert print ("Usuario distinto") 
     time.sleep(2)     
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/button').click() #Cerrar recuadro de perfil
     time.sleep(2)
     print("Revision realizada con éxito")
except:
     print("Problemas en la validación")

#Procesos asignados
""" try:
     driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #ingreso a menú
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/a[4]').click() #Procesos Asignados
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/a').click() #Click en último proceso
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[1]/div[1]/div/div/select/option[3]').click() #Cambio de estado
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[1]/div/textarea').send_keys("Prueba de Campo coach ") #Ingreso texto1
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[2]/div/textarea').send_keys("Prueba de Campo coach ") #Ingreso texto2
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[3]/div/div/div[1]/div/textarea').send_keys("Prueba de Campo coach ") #Ingreso texto3
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[4]/button').click() #Grabar
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[6]/div/div[6]/button[1]').click() #Confirmar
     time.sleep(5)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     driver.find_element_by_xpath('/html/body/div[4]/div/a[1]').click() #Volver
     time.sleep(2)
     print("Proceso asignado con éxito")
except:
     print("Error en la asignación del proceso")""" 

#Seleccion menú
try:
     driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #ingreso a menú
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/a[5]').click() #ingreso a menú
     time.sleep(2)
     
#Buscar por Nombre de la empresa
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/input').send_keys("BigTicket") #ingreso de parametros de búsqueda
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/input').clear()
     time.sleep(2)

#Buscar por nombre del Coachee
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/input').send_keys("Felipe Segura") #Ingreso de parametros de busqueda por nombre de coachee
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/input').clear()
     print("Búsqueda realizada con éxito")
except:
     print("Fallo en la búsqueda solicitada")

#Visualizar procesos
try:
     driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr/th[6]/a/i').click() #Ingreso a visualizacion del proceso
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[1]/div[1]/div/div/select/option[3]').click() #cambio de estado
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[1]/div/textarea').send_keys("PRUEBA DE TEXTO ") #Prueba Objetivo
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[2]/div/textarea').send_keys("PRUEBA DE TEXTO ") #Prueba indicadores
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[3]/div/div/div[1]/div/textarea').send_keys("PRUEBA DE TEXTO ") #Prueba Plan de accion
     time.sleep(2)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[4]/button').click() #guardar
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[6]/div/div[6]/button[1]').click() #Confirmar
     time.sleep(4)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
#Sesión 1
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/p[1]').click() #Información sesión 1
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/div/div[1]/div/input').send_keys("06-12-2021")  #fecha inicio
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/div/div[2]/div/input').send_keys("20:00") #hora inicio
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/select/option[2]').click() #Estado sesion
     time.sleep(2)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[2]/div[1]/div/textarea").send_keys("PRUEBA DE TEXTO") #prueba1
     time.sleep(1)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[2]/div[2]/div/textarea").send_keys("PRUEBA DE TEXTO") #prueba2
     time.sleep(1)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[3]/div[1]/div/textarea").send_keys("PRUEBA DE TEXTO") #prueba3
     time.sleep(2)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/div[2]/button").click() #Guardar sesion1
     time.sleep(2)
     driver.find_element_by_xpath("/html/body/div[6]/div/div[6]/button[1]").click() #confirmar
     time.sleep(5)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(5)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/p[1]').click() #Información sesión 1
     time.sleep(3)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(5)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/form/div/textarea").send_keys(Link1) #Adjuntar Link Prueba
     time.sleep(3)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/form/div/i").click() #Boton de adjuntar
     time.sleep(3)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/p[1]').click() #Información sesión 1
     time.sleep(2)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(3)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/table/tbody/tr/th[1]/a").click()#Abrir link prueba 
     time.sleep(3)
     driver.switch_to.window(driver.window_handles[1])
     time.sleep(10)
     driver.close()
     driver.switch_to.window(driver.window_handles[0])
     time.sleep(3)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     
#Descargar PDF
     driver.find_element_by_xpath("/html/body/div[4]/div/a[2]").click()#Click al boton descargar 
     time.sleep(5)

     driver.find_element_by_xpath('/html/body/div[4]/div/a[1]').click() #Volver a listado 
     time.sleep(2)
     print("visualización, modificación y cdescargas realizadas con éxito")
except:
     print("Problemas con solicitud")

#Salida vista principal
driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #Perfil
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]').click() #Click imagen 
time.sleep(2) 

#cerrar el navegador
driver.quit()

#pytest.exe -v -s --capture=tee-sys --html=CP_N.html --self-contained-html ".\PruebasLoginCoach.py"

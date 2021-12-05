
import time
import pytest
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

driver_path = 'C:\\chromedriver\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciar la en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()

#Credenciales ThinkGo
#Admin
userAdmin = "ne.gomezg@duocuc.cl"
passwordAdmin = "Nels.9876"

#Coach
userCoach = "coachpruebaqa@gmail.com"
passwordCoach = "Dani.9999"

#Coachee
userCoachee = "coacheetestqa@gmail.com"
passwordCoachee = "Feli.9999"

#Credenciales Gmail
#Gmail
userGmail = "coachpruebaqa@gmail.com"
passwordGmail = "Qa123456"

#Links
Link1 = "https://www.youtube.com/watch?v=b4Y6hNOQ_0o"

# Inicializamos el navegador
driver.get('https://www.sistemabitacoracoaching.tk/')
print ("El titulo de la URL-principal es: https://www.sistemabitacoracoaching.tk/")
time.sleep(2)
#driver.get('http://127.0.0.1:8000/')

#Login al servicio con las credenciales del perfil administrador 
try:
     driver.find_element_by_xpath('//*[@id="validationUsername"]').send_keys(userAdmin)
     driver.find_element_by_xpath('//*[@id="validationPassword"]').send_keys(passwordAdmin)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
     time.sleep(2)
     print ("Prueba realizada con exito")
     #except:
          #print("Fallo login")

     #Validación credenciales
     #try:
     driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #ingreso a perfil
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/a[1]').click() #busqueda de correo en perfil
     time.sleep(1)
     usuarioActual = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/input').get_attribute('value') #seleccion de correo en perfil
     time.sleep(2)
     if usuarioActual== userAdmin:
          print ("Usuario correcto")
     else: 
          print ("Usuario distinto") 
     time.sleep(2)     
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/button').click() #Cerrar recuadro de perfil
     time.sleep(2)
     print("Revision realizada con éxito")
     #except:
          #print("Problemas en la validación")
     """ 
     #ingresar al menu del administrador 
     #try:
          driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click()
          time.sleep(2)

     #seleccionar apartado de usuarios del servicio
          driver.find_element_by_xpath('/html/body/div[1]/a[5]').click()
          time.sleep(2)

     #funcionalidad de los botones dentro del apartado
          driver.find_element_by_xpath('/html/body/div[3]/a[2]').click() #Nuevo usuario
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[3]/a[3]').click() #Listar usuarios
          time.sleep(2)

     #funcionalidad de botones dentro del apartado de "nuevo usuarios"
          driver.find_element_by_xpath('/html/body/div[3]/a[2]').click() #Nuevo usuario
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/button').click() #crear usuario coachee
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/button').click() #crear usuario coach
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/button').click() #crear usuario administrador
          time.sleep(2)
          print("Prueba de funcionalidades OK")
     #except:
          print("Error en funcion/es")

     #crear usuario Coach
     #try:
          driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #Ingreso menú
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[1]/a[5]').click() #usuarios
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[3]/a[2]').click() #Nuevo usuario
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/button').click() #crear perfil coach
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/form/div/div[1]/div/div/div[1]/div/input').send_keys("Danilo") #nombre Coach
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/form/div/div[1]/div/div/div[2]/div/input').send_keys("Gómez") #apellido coach
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/form/div/div[2]/div/div/div[1]/div/input').send_keys("coachpruebaqa@gmail.com") #Email coach
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/form/div/div[2]/div/div/div[2]/div/input').send_keys("999999999") #Fono jefe
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/form/div/button').click() #Grabar
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[8]/div/div[6]/button[1]').click()#confirmar usuario
          time.sleep(3)
          print("Usuario creado con éxito")
     #except:
          print("Problemas al crear el usuario")

     #Crear nuevo usuario Coachee
     #try:
          driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/button').click() #crear perfil coachee
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[1]/div[1]/div/input').send_keys("BigTicket") #nombre empresa
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[1]/div[3]/div/div[1]/div/input').send_keys("Felipe") #nombre coachee
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[1]/div[3]/div/div[2]/div/input').send_keys("Segura") #apellido coachee
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[1]/div[4]/div/div[1]/div/input').send_keys("Mauricio") #nombre jefe
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[1]/div[4]/div/div[2]/div/input').send_keys("Figueroa") #apellido jefe
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/div[1]/div/input').send_keys("coacheetestqa@gmail.com") #Email coachee
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/div[2]/div/input').send_keys("mau.figue@bigticket.cl") #correo jefe 
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[3]/div[1]/div/input').send_keys("999999999") #Fono coachee
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[3]/div[2]/div/input').send_keys("999999999") #Fono Jefe
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[5]/div/div/form/button').click() #grabar
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[8]/div/div[6]/button[1]').click()#confirmar usuario
          time.sleep(3)
          print("Usuario creado con éxito")
     #except:
          print("Problemas al crear el usuario")

     #Volver al menu principal del perfil adminitrador 
     #try:
          driver.find_element_by_xpath('/html/body/div[3]/a[1]').click()
          time.sleep(2) """

     #Listar usuario
     #try:
     driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #ingreso Menu
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/a[5]').click() #Usuarios
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/a[3]').click() #Listar usuarios
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[1]/div/input').send_keys("Danilo Gómez") #credenciales de búsqueda 
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[1]/div/input').clear()
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[1]/div/input').send_keys("Felipe segura") #credenciales de búsqueda
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[1]/div/input').clear()
     """ time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[2]').click() #Busqueda por administrador
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[4]').click() #Busqueda por coachee
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[1]').click() #Busqueda todos los perfiles
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select/option[2]').click() #Busqueda por habilitado
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select/option[3]').click() #Busqueda por deshabilitado """
     time.sleep(2)
     print("Listar usuarios OK")
     #except:
          #print("Problemas al listar usuarios")     

     #Volver al menu principal del perfil adminitrador
     #try: 
     driver.find_element_by_xpath('/html/body/div[3]/a[1]').click()
     time.sleep(2)

     #Apartado de  creacion y modificacion de procesos 
     driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #ingreso Menu
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/a[4]').click() #procesos 
     time.sleep(2)

     #Nuevos procesos 
     driver.find_element_by_xpath('/html/body/div[3]/a[2]').click() #nuevo proceso
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/form/div[1]/div/input').send_keys("BigTicket") #nombre empresa
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/form/div[2]/div/input').send_keys("3") #cantidad de sesiones
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/form/div[4]/div/select').send_keys("Danilo Gómez") #selección de coach
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/form/div[5]/div/select').send_keys("Felipe Segura") #selección de coachee
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/form/button').click() #Crear proceso
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[6]/div/div[6]/button[1]').click() #Confirmar proceso
     time.sleep(3)

     #Listar proceso
     driver.find_element_by_xpath('/html/body/div[3]/a[3]').click() #Listar Procesos
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/input').send_keys("Danilo Gómez") #credenciales de búsqueda coach
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/input').clear()
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/input').send_keys("Felipe Segura") #credenciales de búsqueda coachee
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/input').clear()
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/input').send_keys("BigTicket") #credenciales de búsqueda empresa
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/input').clear()
     time.sleep(2)

     #cierre sesión
     driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #perfil
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]').click() #cierre sesión
     time.sleep(2)
     print("Creación y listado de procesos OK")
     #except:
          #print("Problemas en el proceso") 
          #time.sleep(5)
     
     """ #Cambio de contraseña
     #try:
          driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/span/a').click()#Olvido su contraseña
          time.sleep(2)                              
          driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/input').send_keys(userGmail)#Ingreso de correo de recuperación 
          time.sleep(2) 
          driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()#click en recuperar 
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/button[1]').click()#Mensaje de confirmación
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/span/a').click()#Volver al inicio
          time.sleep(2)
          print("Se realiza solicitud de recuperacion de contraseña de manera correcta")
     #except:
          print("Falló solicitud de recuperación")
          time.sleep(3)

     #Cambio de pestaña en el navegador
     #try:
          driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEn#try=ServiceLogin')")
          time.sleep(2)
          driver.switch_to.window(driver.window_handles[1])
          time.sleep(2)
          driver.find_element_by_name("identifier").send_keys(userGmail)
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
          time.sleep(20)
          driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(passwordGmail)
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
          time.sleep(2)
          driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]').click()
          time.sleep(5)
          driver.switch_to.window(driver.window_handles[0])
          time.sleep(5)
          print("Se verifica correo de recuperación OK")
     #except:
          print("Correo no enviado") """

     ############################################################################ PRUEBAS COACH #######################################################################################

     #Login al servicio 
     #try:
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/input').send_keys(userCoach)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/input').send_keys(passwordCoach)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
     print("Prueba realizada con exito")
     #except:
          #print("Fallo login")


     #Validación credenciales
     #try:
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
     #except:
          #print("Problemas en la validación")

     #Procesos asignados
     #try:
     driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #ingreso a menú
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/a[4]').click() #Procesos Asignados
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/a').click() #Click en último proceso
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[1]/div[1]/div/div/select/option[3]').click() #Cambio de estado
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[1]/div/textarea').send_keys("PRUEBA COACH ") #Ingreso texto1
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[2]/div/textarea').send_keys("PRUEBA COACH ") #Ingreso texto2
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[3]/div/div/div[1]/div/textarea').send_keys("PRUEBA COACH ") #Ingreso texto3
     time.sleep(4)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(4)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[4]/button').click() #Grabar
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[6]/div/div[6]/button[1]').click() #Confirmar
     time.sleep(5)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/a[1]').click() #Volver
     time.sleep(5)
     print("Proceso asignado con éxito")
     #except:
          #print("Error en la asignación del proceso") 



     #Buscar por Nombre de la empresa
     #try:
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/input').send_keys("BigTicket") #ingreso de parametros de búsqueda
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/input').clear()
     time.sleep(2)

     #Buscar por nombre del Coachee
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/input').send_keys("Felipe Segura") #Ingreso de parametros de busqueda por nombre de coachee
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/input').clear()
     print("Búsqueda realizada con éxito")
     #except:
          #print("Fallo en la búsqueda solicitada")

     #Visualizar procesos
     #try:
     driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr/th[6]/a/i').click() #Ingreso a visualizacion del proceso
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[1]/div[1]/div/div/select/option[3]').click() #cambio de estado
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[1]/div/textarea').send_keys(" PRUEBA DE TEXTO ") #Prueba Objetivo
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/div/div/div[2]/div/textarea').send_keys(" PRUEBA DE TEXTO ") #Prueba indicadores
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[3]/div/div/div[1]/div/textarea').send_keys(" PRUEBA DE TEXTO ") #Prueba Plan de accion
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
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[2]/div[1]/div/textarea").send_keys(" PRUEBA DE TEXTO") #prueba1
     time.sleep(1)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[2]/div[2]/div/textarea").send_keys(" PRUEBA DE TEXTO") #prueba2
     time.sleep(1)
     driver.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[3]/div[1]/div/textarea").send_keys(" PRUEBA DE TEXTO") #prueba3
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
     driver.find_element_by_xpath("/html/body/div[4]/div/div/a[2]").click()#Click al boton descargar 
     time.sleep(5)

     driver.find_element_by_xpath('/html/body/div[4]/div/div/a[1]').click() #Volver a listado 
     time.sleep(2)
     print("visualización, modificación y cdescargas realizadas con éxito")
     #except:
          #print("Problemas con solicitud")

     #Salida vista principal
     driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #Perfil
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]').click() #Click imagen 
     time.sleep(5)


     ############################################################################ PRUEBAS COACHEE #######################################################################################



     #Login al servicio 
     #try:
     driver.find_element_by_xpath('//*[@id="validationUsername"]').send_keys(userCoachee)
     driver.find_element_by_xpath('//*[@id="validationPassword"]').send_keys(passwordCoachee)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
     print("Prueba realizada con exito")
     #except:
          #print("Fallo login")


     #agregar print de validacion
     #try:

     driver.find_element_by_xpath('/html/body/div[1]/div/button').click() #ingreso a perfil
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/div[1]/div/div/a[1]').click() #busqueda de correo en perfil
     time.sleep(1)
     usuarioActual = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/input').get_attribute('value') #seleccion de correo en perfil
     time.sleep(2)
     if usuarioActual== userCoachee:
          print ("Usuario correcto")
     else: 
          assert print ("Usuario distinto") 
     time.sleep(2)     
     driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click() #Cerrar recuadro de perfil
     time.sleep(2)
     print("Revision realizada con éxito")
     #except:
          #print("Problemas en la validación")

     #Abrir sesión
     #try:
          
     driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/a').click() #Abrir sesión asignada
     time.sleep(2)
     driver.switch_to.window(driver.window_handles[1])
     time.sleep(4)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/form/div/div[3]/div/div[1]/div[1]/div/textarea').send_keys('TEXTO PRUEBA') #Ingresar texto prueba
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/form/div/div[3]/div/div[2]/div/button').click() #Grabar
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div[6]/button[1]').click() #Confirmar
     time.sleep(4)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/p[1]').click() #Sesión 1
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/div/form/div[3]/div[2]/div/textarea').send_keys(' TEXTO PRUEBA') #Ingresar texto prueba
     time.sleep(2)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/div/form/div[5]/button').click() #Grabar
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div[6]/button[1]').click() #Confirmar 
     time.sleep(4)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/a').click() #Cerrar vista sesión
     time.sleep(2)
     driver.switch_to.window(driver.window_handles[0])
     time.sleep(2)
     print("Funcinalidad de sesión, ejecutada de manera correcta")
     #except:
          #print("Problemas en la ejecución")

     #Salir de sesion
     #try:
     driver.find_element_by_xpath('/html/body/div[1]/div/button').click() #Perfil
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/div/div/a[2]').click() #cerrar sesion
     time.sleep(2)




     ########################################## Finalizar sesion Coach ########################################
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/input').send_keys(userCoach)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/input').send_keys(passwordCoach)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
     print("Prueba realizada con exito")
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #ingreso a menú
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/a[5]').click() #Listar Procesos
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr/th[6]/a/i').click() #Click en último proceso

     time.sleep(4)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     #Sesión 1
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/p[1]').click() #Información sesión 1
     time.sleep(3)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/select/option[4]').click() #Cambio de estado
     time.sleep(3)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div/div/div/div[1]/div/div[2]/button').click() #guardar
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[6]/div/div[6]/button[1]').click() #Confirmar
     time.sleep(4)
     driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #Perfil
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]').click() #Click cerrar sesion 
     time.sleep(5)
     print("Finalizar sesión con éxito.")
     ############################################################################ PRUEBAS COACHEE #######################################################################################

     #Login al servicio 
     #try:
     driver.find_element_by_xpath('//*[@id="validationUsername"]').send_keys(userCoachee)
     driver.find_element_by_xpath('//*[@id="validationPassword"]').send_keys(passwordCoachee)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
     print("Prueba realizada con exito")
     time.sleep(3)
     driver.find_element_by_xpath('/html/body/div[1]/div/button').click() #Perfil
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/div/div/a[2]').click() #cerrar sesion
     time.sleep(2)

     #############Ingreso a finalizar el proceso
     driver.find_element_by_xpath('//*[@id="validationUsername"]').send_keys(userAdmin)
     driver.find_element_by_xpath('//*[@id="validationPassword"]').send_keys(passwordAdmin)
     driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
     time.sleep(2)
     print ("Prueba realizada con exito")
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[2]/div/button[1]').click() #ingreso Menu
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[1]/a[4]').click()#Ingreso Procesos
     #Listar proceso
     driver.find_element_by_xpath('/html/body/div[3]/a[3]').click() #Listar Procesos
     time.sleep(2)
     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/input').send_keys("BigTicket") #credenciales de búsqueda empresa
     time.sleep(2)
     driver.execute_script('''document.querySelector("#example > tbody > tr > th:nth-child(8) > i").click();''')
     time.sleep(3) 
     driver.find_element_by_xpath('/html/body/div[5]/div/div[14]/div/div/div[3]/a').click()
     time.sleep(6)
     driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #Perfil
     time.sleep(1)
     driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]').click() #Click cerrar sesion 
     time.sleep(5)
     print("Finalizar sesión con éxito.")
     print("Cierre de sesión generado de manera correcta")
     assert 'cierre' == 'cierre'
               
     #cerrar el vanegador
     driver.quit()
except:
     print("Problemas con el cierre")



     


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

# Iniciar la en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()

#Credenciales ThinkGo
#Admin
userAdmin = "ne.gomezg@duocuc.cl"
passwordAdmin = "Nels.9876"

#Credenciales Gmail
#Gmail
userGmail = "admpruebaqa@gmail.com"
passwordGmail = "Qa123456"
# Inicializamos el navegador
driver.get('https://www.sistemabitacoracoaching.tk/')
print ("El titulo de la URL-principal es: https://www.sistemabitacoracoaching.tk/")
time.sleep(2)
#driver.get('http://127.0.0.1:8000/')

#Login al servicio con las credenciales del perfil administrador 
driver.find_element_by_xpath('//*[@id="validationUsername"]').send_keys(userAdmin)
driver.find_element_by_xpath('//*[@id="validationPassword"]').send_keys(passwordAdmin)
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
time.sleep(2)

#Validación credenciales
driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #ingreso a perfil
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/a[1]').click() #busqueda de correo en perfil
time.sleep(1)
usuarioActual = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/input').get_attribute('value') #seleccion de correo en perfil
time.sleep(2)
if usuarioActual== userAdmin:
     print ("Usuario correcto")
else: 
     assert print ("Usuario distinto") 
time.sleep(2)     
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/button').click() #Cerrar recuadro de perfil
time.sleep(2)

#ingresar al menu del administrador 
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

#crear usuario Coach
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

#Crear nuevo usuario Coachee
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

#Volver al menu principal del perfil adminitrador 
driver.find_element_by_xpath('/html/body/div[3]/a[1]').click()
time.sleep(2)

#Listar usuario
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
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[2]').click() #Busqueda por administrador
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[4]').click() #Busqueda por coachee
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[1]').click() #Busqueda todos los perfiles
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select/option[2]').click() #Busqueda por habilitado
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select/option[3]').click() #Busqueda por deshabilitado
time.sleep(2)

#Volver al menu principal del perfil adminitrador 
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
driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/form/div[2]/div/input').send_keys("4") #cantidad de sesiones
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

#Cambio de contraseña
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/span/a').click()#Olvido su contraseña
time.sleep(2)                              
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/input').send_keys("AdmpruebaQA@gmail.com")#Ingreso de correo de recuperación 
time.sleep(2) 
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()#click en recuperar 
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/button[1]').click()#Mensaje de confirmación
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/span/a').click()#Volver al inicio
time.sleep(2)
print("Se realiza solicitud de recuperacion de contraseña")

#Cambio de pestaña en el navegador
driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.find_element_by_name("identifier").send_keys(userGmail)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(passwordGmail)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
print ("Se recepciona correo por solicitud de cambio de contraseña de manera correcta")
time.sleep(5) 


#cerrar el navegador
driver.quit()

#pytest.exe -v -s --capture=tee-sys --html=CP_N.html --self-contained-html ".\PruebasAdmin.py"
#pruebas unitarias, usen dentro del venv python manage.py test
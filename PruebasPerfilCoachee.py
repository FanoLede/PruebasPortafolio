
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



# #Credenciales
# #Admin
# user = "ne.gomezg@duocuc.cl"
# password = "Nels.9876"

# #Coach
# user = "c.jatib@duocuc.cl"
# password = "Carl.9719"

#Coachee
userCoachee = "felipito@gmail.com"
passwordCoachee = "Feli.9999"

# Inicializamos el navegador
#driver.get('https://www.sistemabitacoracoaching.tk/')
driver.get('http://127.0.0.1:8000/')


#Login al servicio 
driver.find_element_by_xpath('//*[@id="validationUsername"]').send_keys(userCoachee)
driver.find_element_by_xpath('//*[@id="validationPassword"]').send_keys(passwordCoachee)
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/button').click()

#agregar print de validacion
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

#Salir de sesion
driver.find_element_by_xpath('/html/body/div[1]/div/button').click() #Perfil
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/a[2]').click() #cerrar sesion
time.sleep(2)

# #Salir de sesion
driver.find_element_by_xpath('/html/body/div[1]/div/button').click() #Perfil
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/a[2]').click() #cerrar sesion
time.sleep(2)

#cerrar el vanegador
driver.quit()


#      #pytest.exe -v -s --capture=tee-sys --html=CP_N.html --self-contained-html ".\PruebasLoginCoachee.py"
#try: 
#       print("Funciono")
# except AssertionError:
#       print("Oops!  Hubo un error con el CP001")

# driver.get('http://127.0.0.1:8000/infoProCoachee/6/')

# driver.find_element_by_xpath('/html/body/div[2]/form/div').click() #Nueva pestaña
# time.sleep(2)



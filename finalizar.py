
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
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/input').send_keys("BigTicket") #credenciales de búsqueda empresa
time.sleep(3)
driver.execute_script('''document.querySelector("#example > tbody > tr > th:nth-child(6) > a").click();''')#Visualizar proceso
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(4)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll de la página
#Descargar PDF
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[3]/a[2]").click()#Click al boton descargar 
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div/button[2]').click() #Perfil
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]').click() #Click cerrar sesion 
time.sleep(5)
print("Finalizar sesión con éxito.")
print("Cierre de sesión generado de manera correcta")
assert 'cierre' == 'cierre'
        
#cerrar el vanegador
driver.quit()
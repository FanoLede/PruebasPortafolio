
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
user = "ne.gomezg@duocuc.cl"
password = "Nels.9876"

# #Coach
# user = "c.jatib@duocuc.cl"
# password = "Carl.9719"

# #Coachee
# user = "s.ledezma@duocuc.cl"
# password = "Stef.9494"

# Inicializamos el navegador
#driver.get('https://www.sistemabitacoracoaching.tk/')
driver.get('http://127.0.0.1:8000/')

#Login al servicio 
driver.find_element_by_xpath('//*[@id="validationUsername"]').send_keys(user)
driver.find_element_by_xpath('//*[@id="validationPassword"]').send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/button').click()


assert driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').is_displayed() == True
time.sleep(2)

#Seleccion menú
driver.find_element_by_xpath('//*[@id="main"]/div/button[1]').click()
time.sleep(2)
#Seleccion apartado Usuarios
driver.find_element_by_xpath('/html/body/div[1]/a[5]').click()
time.sleep(2)
#Listar Ususarios
driver.find_element_by_xpath('/html/body/div[3]/a[3]').click()
time.sleep(3)
#Buscar por Nombre
# driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[1]/div/input').click()
# driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[1]/div/input').send_keys("Marcelo Fuentes")
# time.sleep(3)
# driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[1]/div/input').send_keys("Victor González")
# time.sleep(5)
#Buscar por tipo de Usuario
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select').click()
# driver.find_elements('/html/body/div[4]/div/form/div/div[2]/div/select').send_keys("Administrador").click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[2]').click()
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select/option[1]').click()
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[2]/div/select').click()
time.sleep(2)
#Listar por estado
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select/option[2]').click()
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[5]/div/div[6]/div[1]/div[2]/table/tbody/tr[5]/th[6]/i').click()
time.sleep(2)

contacto = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[2]/div/div/div[1]/div[6]/div/input').get_text('value')
if 999631714 == contacto:
    print ('El usuario fue seleccionado con exito', contacto)

else:
    print ('El usuario seleccionado no es el correcto')
# #desabilitar
# radio1 = driver.find_element_by_xpath('/html/body/div[5]/div/div[10]/div/div/div[2]/div/div/div[4]/div/input')
# radio1.click()
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/div/div[10]/div/div/div[3]/button[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[10]/div/div[6]/button[1]').click()
# time.sleep(2)
# #Listar por estado
# # driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select').click()
# # time.sleep(2)
# # driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select/option[3]').click()
# # driver.find_element_by_xpath('/html/body/div[4]/div/form/div/div[3]/div/select').click()
# # time.sleep(2)
# # driver.find_element_by_xpath('/html/body/div[5]/div/div[15]/div[1]/div[2]/table/tbody/tr[3]/th[6]/i').click()
# # time.sleep(3)
# # #habilitar
# # radio1 = driver.find_element_by_xpath('/html/body/div[5]/div/div[15]/div[1]/div[2]/table/tbody/tr[1]/th[6]/i')
# # radio1.click()
# # time.sleep(1)
# # driver.find_element_by_xpath('/html/body/div[5]/div/div[10]/div/div/div[3]/button[2]').click()
# # time.sleep(2)
# # driver.find_element_by_xpath('/html/body/div[10]/div/div[6]/button[1]').click()
# # time.sleep(2)
# # driver.find_elements_by_css_selector('#exampleModal-10 > div > div > div.modal-footer > button.btn.btn-primary').click
# # time.sleep(2)



#cerrar el vanegador
driver.quit()


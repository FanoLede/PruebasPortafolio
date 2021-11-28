# PruebasPortafolio

                                                                ▔▔▔▔▔╲
                                                                ▕╮╭┻┻╮╭┻┻╮╭▕╮╲
                                                                ▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏
                                                                ▕╭┻┻┻┛┗┻┻┛ ▕ ╰▏
                                                                ▕╰━━━┓┈┈┈╭╮▕╭╮▏
                                                                ▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏
                                                                ▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏          

Bienvenido a las pruebas de portafolio, para poder realizar la ejecución de las pruebas, se requiere de los sigue


Para poder ejecutar estas pruebas debe cumplir con los requerimientos minimos:

    Instalacion

        1)  Instalar Python 3.8.x, lo puede descargar desde el siguiente link =>  https://www.python.org/downloads/
        2)  Instalar el administrador de paquetes PIP con el siguiente comando ==>> python -m pip install --upgrade pip
        3)  Ahora con pip instalado podra instalar la libreria de selenium en el ambiente de pruebas  ----- > pip install selenium
        4)  Descargar chromedriver desde el siguiente link segun su versión de google chrome => https://chromedriver.chromium.org/downloads 
            Opcionalmente, deje en una ruta/directorio/carpeta deseada.
        5)  Abrir los archivos de prueba .py dentro del proyecto, editar el campo driver_path y dentro de este agregar la ruta donde se encuentra chromedriver.

                EJEMPLO: 

                ---------------------------------------PORCIÓN DE CODIGO---------------------------------

                                        # Opciones de navegación
                                        options =  webdriver.ChromeOptions()
                                        options.add_argument('--start-maximized')
                                        options.add_argument('--disable-extensions')

                                        driver_path = 'C:\\Users\\56949\\Downloads\\chromedriver.exe'

                                        driver = webdriver.Chrome(driver_path, chrome_options=options)

                ---------------------------------------PORCIÓN DE CODIGO---------------------------------

    Para ejecutar las prueba:

        1)  Abrir la consola de preferencia, ya sea cmd,powershell,etc..
        2)  Ir al directorio donde estan ubicadas fisicamente los archivos de prueba con el comando cd para moverse dentro de directorios.
                Ejemplo de uso => cd C:\Program Files
        3)  Para ejecutar la prueba, escriba el nombre del archivo dentro del siguiente comando=> python EscribaNombreDeArchivo.py
        4)  En caso de no poder ejecutar las pruebas, vuelva a verificar las instrucciones o contactese con soporte.
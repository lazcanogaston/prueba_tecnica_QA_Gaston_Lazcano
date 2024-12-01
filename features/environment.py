from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.logger import Logger
import csv
import os
from datetime import datetime

def before_feature(context, feature):
    try:
        # Usa WebDriverManager para obtener el chromedriver y crear el servicio
        driver_path = ChromeDriverManager().install()
        # Crea el servicio y el WebDriver
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service)
        context.driver.maximize_window()
        #LOG Y SCREENSHOT
        context.logger = Logger._init_logger_txt("LOG_Alten")
        context.screenshot = Logger.take_screenshot_and_log(context.driver, context.logger, log_message="screenshot taken")
        context.logger.info("Webdriver is open and maximized.")
       # screenshot_path = Logger.take_screenshot_and_log(context.driver, context.logger, log_message="Homepage loaded")
        # Registramos la captura de pantalla en el log
      #  context.logger.info(f"Screenshot saved at: {screenshot_path}")
        
    except Exception as e:
        context.logger.error(f"Error al inicializar el WebDriver: {e}")
        raise

def after_feature(context, feature):
    context.driver.quit()

CSV_FILE_PATH = 'test_report.csv'

def after_scenario(context, scenario):
    """Hook para grabar los resultados de cada escenario después de la ejecución"""
    
    # Si el archivo no existe, creamos el archivo CSV y escribimos los encabezados
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribimos los encabezados
            writer.writerow(['Execution Time', 'Feature', 'Scenario', 'Result'])
    
    # Guardamos la información de cada ejecución
    with open(CSV_FILE_PATH, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Obtiene el tiempo de ejecución actual
        execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Escribe los resultados de la ejecución
        writer.writerow([execution_time, scenario.feature.name, scenario.name, scenario.status])
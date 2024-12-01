import datetime
import logging
import os

class Logger():
    
    # to use next method -> in tests, use StringIO logger (log in memory)
    # import io
    # logStringio = io.StringIO()

    def _init_logger(log_stringio_obj, logger_name):
        #creates or open the log 
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        #give format to each line of the log time - level - message
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        #initialize the handler
        io_log_handler = logging.StreamHandler(log_stringio_obj)
        #give the format to the handler
        io_log_handler.setFormatter(formatter)
        #attach the handler to the logger instance
        logger.addHandler(io_log_handler)
        return logger

    def _init_logger_txt(fileName):
        logger = logging.getLogger('name_%s' % fileName)  #1
        logger.setLevel(logging.INFO)  #2
        handler = logging.FileHandler("C:\\Users\\Administrator\\Desktop\\prueba_tecnica_QA_Gaston_Lazcano\\"+fileName+".log") #3
        handler.setLevel(logging.INFO)  #4
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s') #5
        handler.setFormatter(formatter)  #6
        logger.addHandler(handler)  #7
        return logger
    
    @staticmethod
    def take_screenshot_and_log(driver, logger, screenshot_dir="screenshots", log_message="Screenshot captured"):
        
        # Asegurarse de que el directorio de capturas de pantalla exista
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        # Generar un nombre único para la captura de pantalla
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        
        # Tomar la captura de pantalla
        driver.get_screenshot_as_file(screenshot_path)
        
        # Registrar el evento en el log
        logger.info(f"{log_message}: {screenshot_path}")
        
        return screenshot_path
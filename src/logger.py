import logging, os
from datetime import datetime

file = os.path.join(os.getcwd(),"LOGS")
os.makedirs(file,exist_ok=True)

format = f"{datetime.now().strftime('%d-%m-%y %H:%M:%S')}.logs"

file_path = os.path.join(os.getcwd(),"LOGS",format)

logging.basicConfig(
                    filename=file_path,
                    format="[%(asctime)s] [%(lineno)s] %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    )
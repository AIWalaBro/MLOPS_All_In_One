import logging
import sys
import os
from datetime import datetime

try:
    log_file = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
    log_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_path, exist_ok=True)

    LOGFILE_PATH = os.path.join(log_path, log_file)

    logging.basicConfig(
        level=logging.INFO,
        format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOGFILE_PATH),
            logging.StreamHandler(sys.stdout)
        ]
    )
except Exception as e:
    print(f"An error occurred while setting up logging: {e}")
    sys.exit(1)

# Rest of your code goes here

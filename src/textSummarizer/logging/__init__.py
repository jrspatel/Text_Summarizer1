import os
import sys
import logging

logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]' 
# creating the log path 
log_dir = 'logs' 
log_filepath = os.path.join(log_dir,'running_logs.log')
os.makedirs(log_dir, exist_ok=True) 

logging.basicConfig(
    # log information
    level = logging.INFO,
    format= logging_str,

    handlers=[
        # stores the logging info in the file
        logging.FileHandler(log_filepath),
        # shows the logging info on the terminal
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('textSummarizerLogger')


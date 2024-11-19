import logging
import os
from datetime import datetime

# Assuming 'from_root' is a function that gives you the root directory of the project
from from_root import from_root  

# Generate log filename based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory relative to the project root
log_dir = os.path.join(from_root(), 'logs')  # Full path to 'logs' folder

# Ensure the 'logs' directory exists
if not os.path.exists(log_dir):
    print(f"Directory {log_dir} does not exist. Creating it now...")
    os.makedirs(log_dir, exist_ok=True)

# Full path to the log file
logs_path = os.path.join(log_dir, LOG_FILE)

# Setup logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Debugging line: Print the log file path to confirm it's correct
print(f"Logging to file: {logs_path}")

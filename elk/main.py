import logging
from logstash import TCPLogstashHandler
import socket
import time
import random
import json
from datetime import datetime

# Set up a logger for Logstash
logger = logging.getLogger("python-logstash-logger")
logger.setLevel(logging.INFO)

# Add console handler to display logs in terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Send logs to Logstash using the TCP
logstash_handler = TCPLogstashHandler("localhost", 5050, version=1)
logger.addHandler(logstash_handler)

# Example log messages with extra fields
extra = {
    "app_name": "my_python_app",
    "environment": "development",
    "user_id": "user123",
}

# Generate some sample logs
for i in range(5):
    # Randomly choose log level
    level = random.choice(["INFO", "WARNING", "ERROR"])
    message = f"Sample log message {i+1} with level {level}"

    # Add some random extra data
    extra["request_id"] = f"req_{random.randint(1000, 9999)}"
    extra["response_time"] = random.uniform(0.1, 2.0)

    # Create a structured log message
    log_data = {
        "message": message,
        "level": level,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        **extra,
    }

    # Log the structured data
    logger.info(json.dumps(log_data), extra=extra)

    time.sleep(1)  # Wait a second between logs

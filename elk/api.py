import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pythonjsonlogger import jsonlogger
from logstash import TCPLogstashHandler
import sys

# Configure logging
logger = logging.getLogger("FastAPI-Logger")
logger.setLevel(logging.INFO)

def structure_log(**data):
    log_data = {
        "message": data.get("message"),
        "level": data.get("level", "INFO"),
        "timestamp": data.get("timestamp"),
        "path": data.get("path"),
        "status": data.get("status"),
    }
    return log_data


try:
    # Send logs to Logstash using the TCP
    logstash_handler = TCPLogstashHandler("localhost", 5050, version=1)
    logger.addHandler(logstash_handler)
except Exception as e:
    print(f"Error setting up handlers: {e}", file=sys.stderr)
    logger.addHandler(logging.StreamHandler())

# Always add console handler for local debugging
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

app = FastAPI()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    log_data = structure_log(
        path=request.url.path, error=str(exc), status="error"
    )
    logger.error(log_data)
    return JSONResponse(
        status_code=500,
        content={"detail": "An error occurred, please try again later."},
    )


@app.get("/")
async def root():
    log_data = structure_log(path="/", status="success")
    logger.info(log_data)
    return {"message": "Hello, ELK!"}


@app.get("/test")
async def test_endpoint():
    log_data = structure_log(path="/test", status="success", test_data={"value": 42})
    logger.info(log_data)
    return {"message": "Test endpoint working!"}

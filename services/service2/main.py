from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(
    filename='/var/log/fastapi-service2.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@app.get("/")
def read_root():
    logging.info("Root endpoint was accessed in service2")
    return {"Hello": "Service2"}

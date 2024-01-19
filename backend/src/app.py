from fastapi import FastAPI

from src.api import setup_api
import logging


app = FastAPI()
setup_api(app)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

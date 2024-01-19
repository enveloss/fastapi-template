from pydantic import BaseModel

class Config(BaseModel):
    db_conn_string: str

with open('../config.json', encoding='utf-8') as file:
    config = Config.model_validate_json(file.read())
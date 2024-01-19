import uvicorn

def start_dev():
    uvicorn.run('src.app:app', reload=True)

def start_prod():
    uvicorn.run('src.app:app', host='0.0.0.0', port=80)
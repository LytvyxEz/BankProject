from uvicorn import run

if __name__ == '__main__':
    run(app='api.main:app', host='localhost', port=8080, reload=True)
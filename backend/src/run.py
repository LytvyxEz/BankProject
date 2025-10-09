from uvicorn import run

from database.init_db import init_db

if __name__ == '__main__':
    init_db()
    run(app='api.main:app', host='localhost', port=8080, reload=True)
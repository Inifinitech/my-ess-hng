from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from datetime import datetime

app = FastAPI()

required_details = {
    1: {
        "email": "kuriaisac@gmail.com",
        "local-time": "",
        "github-url": "https://github.com"
    }
}

@app.get('/')
def home():
    try: 
        return ORJSONResponse(
            {"message": "Welcome"}, status_code=200
        )
    except Exception as err:
        return ORJSONResponse(
            {"error": f"{str(err)}"}, status_code=500
        )
    
@app.get('/get-details')
def details():
    try:
        required_details[1]["local-time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return ORJSONResponse(required_details[1])
    except Exception as err:
        return ORJSONResponse(
            {"error": f"{str(err)}"}, status_code=500
        )

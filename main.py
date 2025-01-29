from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

required_details = {
    1: {
        "email": "kuriaisac@gmail.com",
        "current_datetime": "",
        "github_url": "https://github.com/Inifinitech/my-ess-hng"
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
        required_details[1]["current_datetime"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        return ORJSONResponse(required_details[1])
    except Exception as err:
        return ORJSONResponse(
            {"error": f"{str(err)}"}, status_code=500
        )

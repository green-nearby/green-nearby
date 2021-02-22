# green-nearby
Get a list of the closest green spaces near you.

## Steps to get the website up

* Activate the pipenv environment with `pipenv shell`

* Run the fastapi server with the command `uvicorn api:app` --reload (make sure the GOOGLE_API_KEY is an env variable)

* In a seperate window run the command `python app.py` (make sure MAPBOX_TOKEN is an env variable)

* Navigate to [http://127.0.0.1:8050/](127.0.0.1:8050)
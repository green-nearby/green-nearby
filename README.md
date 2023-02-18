# green-nearby
Get a list of the closest green spaces near you.

## Steps to get the website up

You'll want to have `MAPBOX_TOKEN` and `GOOGLE_API_TOKEN` defined in your `.env` file.

New way:

```
uvicorn src.green_nearby.app:app --reload
```
or
```
docker compose up --build
```

Navigate to [http://localhost:8000/](localhost:8000)

Old way:
* Run the fastapi server with the command `uvicorn api:app` --reload (make sure the GOOGLE_API_KEY is an env variable)
* In a separate window run the command `python app.py` (make sure MAPBOX_TOKEN is an env variable)
* Navigate to [http://127.0.0.1:8050/](127.0.0.1:8050)


## Development

### Installation

Good to have `pip-tools` installed in your environment (suggestion: `pipx install pip-tools`).  Suggest running a virtualenv, or doing everything by Docker container.

```
pip-sync requirements.txt
```

## Updating dependencies

```
pip-compile --generate-hashes requirements.in
```

# green-nearby

Get a list of the closest green spaces near you.


# Running locally

```
cd src/api/
# Run via Python
pipenv run src/green_nearby/app.py
# Run via Docker<LeftMouse>
docker build -t green-nearby/api .
docker run -it -p 8080:80 --env-file=.env green-nearby/api
```

```
cd src/frontend/
# Run via Python
pipenv run src/green_nearby/app.py
# Run via Docker

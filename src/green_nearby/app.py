import logging

import fastapi
import uvicorn
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.responses import RedirectResponse

from src.green_nearby import api, dash

app = fastapi.FastAPI()
logger = logging.getLogger("api")
logger.setLevel(logging.INFO)

app.include_router(api.router, prefix="/greenspace")
app.mount("/dash", WSGIMiddleware(dash.app.server))


@app.get("/")
async def redirect():
    response = RedirectResponse(url='/dash')
    return response

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

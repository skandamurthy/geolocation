from fastapi import FastAPI
from routers import geocoding


def import_routes(app: FastAPI) -> None:
    # We can keep adding as many API end-points we need
    app.include_router(geocoding.router)

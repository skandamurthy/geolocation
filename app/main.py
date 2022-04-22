from fastapi import FastAPI
from .dependencies import fetch_config
from .import_routes import import_routes

# Create FastAPI app
app = FastAPI()


app.fetch_config = fetch_config


@app.on_event("startup")
async def startup_event() -> None:
    """
    Call startup functions
    """
    import_routes(app)

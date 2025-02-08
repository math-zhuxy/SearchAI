import fastapi
import pydantic

class SERVER:
    def __init__(self):
        self.app = fastapi.FastAPI()
        self.app.mount("/static", fastapi.staticfiles.StaticFiles(directory="public/static"), name="static")
        template = fastapi.templating.Jinja2Templates(directory="public")
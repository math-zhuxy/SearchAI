import fastapi
import fastapi.staticfiles
import fastapi.templating
import LLMmodel

class SERVER:
    def __init__(self):
        self.app = fastapi.FastAPI()
        self.app.mount("/static", fastapi.staticfiles.StaticFiles(directory="public/static"), name="static")
        template = fastapi.templating.Jinja2Templates(directory="public")

        @self.app.get("/")
        async def index(request: fastapi.Request):
            return template.TemplateResponse("main.html", {"request": request})

        @self.app.get("/chat")
        async def process_message(input: str):
            return LLMmodel.model_communicate(input)
        
        @self.app.get("/test")
        async def test(): 
            return {"message": "connection successful"}  
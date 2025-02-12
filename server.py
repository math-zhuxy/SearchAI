import fastapi
import fastapi.staticfiles
import fastapi.templating
import LLMmodel
import pydantic
import set

class MSG(pydantic.BaseModel):
    msg: str

class SERVER:
    def __init__(self):
        self.app = fastapi.FastAPI()
        self.app.mount("/static", fastapi.staticfiles.StaticFiles(directory="public/static"), name="static")
        template = fastapi.templating.Jinja2Templates(directory="public")

        @self.app.get("/")
        async def index(request: fastapi.Request):
            return template.TemplateResponse("main.html", {"request": request})
        
        @self.app.get("/init")
        async def initing():
            return {
                "key": set.user_api_key[:20]+"...",
                "nam": set.model_name,
                "url": set.model_url[:20]+"...",
                "tool": set.func_call_choice,
                "sys": set.system_message,
                "func": set.function_description,
                "par": set.func_parameter_description
            }

        @self.app.post("/chat")
        async def process_message(mg: MSG):
            return {"msg": LLMmodel.model_communicate(mg.msg)}
        
        @self.app.get("/test")
        async def test(): 
            return {"msg": "connection successful"}  
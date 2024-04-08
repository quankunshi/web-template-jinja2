from fastapi import FastAPI, Request, Form
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Khởi tạo Jinja2Templates với thư mục chứa templates
templates = Jinja2Templates(directory="templates")
app.mount("/statics", StaticFiles(directory="statics"), name="statics")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Render template với Jinja
    return templates.TemplateResponse(name="index.html", context={"request": request,"sentiment":"pos"})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request, item: str = Form(...)):
    # Xử lý dữ liệu từ form và render template với Jinja
    return templates.TemplateResponse("submit.html", {"request": request, "item": item})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
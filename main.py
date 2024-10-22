from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Путь к файлу для сохранения данных
data_file_path = "user_data.txt"

@app.get("/", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/")
async def create_user(username: str = Form(...), password: str = Form(...)):
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password are required")

    # Записываем данные в файл
    with open(data_file_path, "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return {"username": username, "message": "Data saved successfully"}

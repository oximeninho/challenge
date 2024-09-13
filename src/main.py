from fastapi import FastAPI, Request
import psycopg
import requests
import uvicorn

app = FastAPI()

# URL do webhook local
WEBHOOK_URL = "http://api:8000/webhook"
# URL da API para iniciar uma nova sessão
SESSION_API_URL = "http://waha-container:3000/api/sessions/"
# URL da API para enviar uma mensagem de texto
SEND_TEXT_API_URL = "http://waha-container:3000/api/sendText"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()
    grupo = body["payload"]["from"]
    grupo_desejado = "1629810428@g.us"
    data = body["payload"]["body"]    
    # Divide a string no caractere '-'
    partes = grupo.split('-')
    
    # Verifica se há uma parte após o '-'
    if len(partes) > 1:
        grupo_recebido = partes[1]
        
        # Verifica se a parte após '-' corresponde ao grupo desejado
        if grupo_recebido == grupo_desejado:
            insert_message(data)
    return {"status": "json recebido"}

@app.get("/start-session")
async def start_session():
    payload = {
        "name": "default",
        "start": True,
        "config": {
            "proxy": None,
            "debug": False,
            "noweb": {
                "store": {
                    "enabled": True,
                    "fullSync": False
                }
            },
            "webhooks": [
                {
                    "url": WEBHOOK_URL,
                    "events": [
                        "message",
                        "session.status"
                    ],
                    "hmac": None,
                }
            ]
        }
    }
    response = requests.post(SESSION_API_URL, json=payload)
    print(response.status_code)
    print(response.text)
    return "ok"

@app.post("/send-test-message")
async def send_test_message():
    payload = {
        "chatId": "5521979193228@c.us",
        "text": "Teste de mensagem!",
        "session": "default"
    }
    r = requests.post(SEND_TEXT_API_URL, json=payload)
    
    print(r.status_code)
    print(r.text)
    return {"status": "message sent"}

sqlCreateTable = ''' 
CREATE TABLE IF NOT EXISTS Mensagens (
data text not null, 
inserted_at timestamptz not null default now()
);
 '''

sqlInsertMensagem = '''
insert into Mensagens(data) values('teste');
 '''

def insert_message(mensagem):
    try:
        with psycopg.connect(
            dbname="postgres", user="postgres", password=1234, host="db", port=5432
        ) as conn:
            conn.autocommit = True
            # Criando um cursor usando o método cursor()
            with conn.cursor() as cursor:
                cursor.execute(f"insert into Mensagens(data) values('{mensagem}');")
    except Exception as e:
        print("Ocorreu um erro:", e) 

def create_table():
    try:
        with psycopg.connect(
            dbname="postgres", user="postgres", password=1234, host="db", port=5432
        ) as conn:
            conn.autocommit = True
            # Criando um cursor usando o método cursor()
            with conn.cursor() as cursor:
                cursor.execute(sqlCreateTable)
    except Exception as e:
        print("Ocorreu um erro:", e) 

create_table()
uvicorn.run(app, port=8000, host="0.0.0.0")
 
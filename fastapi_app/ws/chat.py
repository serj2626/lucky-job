# fastapi_app/ws/chat.py
from fastapi import WebSocket, WebSocketDisconnect
from fastapi import APIRouter
import json 
from fastapi import Query

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    async def send_personal_message(self, message: str, user_id: int):
        if conn := self.active_connections.get(user_id):
            await conn.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    # Проверка токена (ваша логика)
    user = authenticate_user(token)
    if not user:
        await websocket.close(code=1008)
        return

    await manager.connect(user.id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # Обработка разных типов сообщений
            if data["type"] == "chat:send":
                await manager.send_personal_message(
                    json.dumps(
                        {
                            "type": "chat:message",
                            "text": data["text"],
                            "senderId": user.id,
                        }
                    ),
                    data["recipientId"],
                )
    except WebSocketDisconnect:
        del manager.active_connections[user.id]

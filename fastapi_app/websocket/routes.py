from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .manager import manager
from typing import Optional

router = APIRouter()

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Обработка входящих сообщений
            await manager.send_personal_message(f"You wrote: {data}", user_id)
    except WebSocketDisconnect:
        manager.disconnect(user_id, websocket)
        await manager.broadcast(f"User #{user_id} left the chat")
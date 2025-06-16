import type {
  ClientToServerEvents,
  ServerToClientEvents,
} from "~/types/socket";

import type { Socket } from "socket.io-client";

export function useChat() {
  const socket = useSocket<
    ServerToClientEvents,
    ClientToServerEvents
  >() as Socket<ServerToClientEvents, ClientToServerEvents>;
  const messages = ref<Array<{ id: string; text: string }>>([]);
  const isConnected = ref(false);

  // Подключение
  const connect = () => {
    if (!socket.connected) {
      socket.connect();
    }
  };

  // Отключение
  const disconnect = () => {
    if (socket.connected) {
      socket.disconnect();
    }
  };

  // Слушатели событий
  socket.on("connect", () => {
    isConnected.value = true;
    console.log("WebSocket connected");
  });

  socket.on("disconnect", () => {
    isConnected.value = false;
    console.log("WebSocket disconnected");
  });

  socket.on("chat:message", (msg) => {
    messages.value.push(msg);
  });

  // Методы для чата
  const sendMessage = (text: string, recipientId: number) => {
    socket.emit("chat:send", { text, recipientId });
  };

  const sendTyping = (recipientId: number) => {
    socket.emit("chat:typing", recipientId);
  };

  return {
    socket,
    messages,
    isConnected,
    connect,
    disconnect,
    sendMessage,
    sendTyping,
  };
}

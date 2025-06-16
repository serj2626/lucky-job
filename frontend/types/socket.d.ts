declare module '#app' {
  interface NuxtApp {
    $socket: import('socket.io-client').Socket
  }
}

// Типы для событий чата
export interface ServerToClientEvents {
  'chat:message': (payload: { id: string; text: string; senderId: number; timestamp: string }) => void
  'chat:typing': (userId: number) => void
  'chat:read': (messageId: string) => void
}

export interface ClientToServerEvents {
  'chat:send': (payload: { text: string; recipientId: number }) => void
  'chat:typing': (recipientId: number) => void
  'chat:read': (messageId: string) => void
}
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-05-15",
  devtools: { enabled: true },

  modules: [
    "@nuxt/eslint",
    "@nuxt/icon",
    "@nuxt/image",
    "@nuxt/ui",
    "nuxt-swiper",
    "@nuxtjs/sitemap",
    "nuxt-schema-org",
    "@pinia/nuxt",
    "nuxt-socket-io",
  ],
  io: {
    sockets: [
      {
        name: "main", // Название соединения
        url: process.env.WS_URL || "ws://localhost:8001", // URL вашего FastAPI сервера
        default: true,
        cors: {
          origin: "*", // Для разработки. В продакшене укажите конкретные домены
        },
        // Доп. настройки Socket.IO
        ioOptions: {
          reconnection: true,
          reconnectionAttempts: 5,
          autoConnect: false, // Подключаем вручную после авторизации
          transports: ["websocket"],
          auth: (cb) => {
            const token = useAuthToken(); // Ваш токен из стора
            cb({ token });
          },
        },
      },
    ],
  },
});

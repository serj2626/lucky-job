# 🧠 Lucky Job — Платформа для поиска работы программистами

Lucky Job — это современная платформа, которая объединяет разработчиков и IT-компании. Система поддерживает real-time общение через WebSocket, уведомления, новостную ленту, фильтрацию вакансий и профилей, а также мощную админку для компаний и HR.

## Проект на стадии разработки 🚧

## 🚀 Стек технологий

| Компонент     | Технология             |
| ------------- | ---------------------- |
| Backend (API) | Django (REST), PostgreSQL |
| Real-time     | FastAPI + WebSocket + Redis |
| Frontend      | Nuxt 3 + TailwindCSS   |
| Auth          | JWT / OAuth2           |
| DevOps        | Docker, docker-compose |

---

## 🧱 Архитектура
┌────────────┐ ┌───────────────┐ ┌─────────────┐
│ Nuxt 3 │ ⇄ HTTP ⇄│ Django API │ │ PostgreSQL │
│ (Frontend) │ │ (Auth, Models)│ │ (Data) │
└────┬───────┘ └──────┬────────┘ └────┬────────┘
│ │ │
│ Redis Pub/Sub │ │
│ ⇅ ▼ ▼
│ ┌────────────────────────┐ ┌──────────────┐
└─────⇄ │ FastAPI (WS) │ ⇄ WS ⇄ │ Nuxt 3 │
│ Чаты, уведомления, │ │ WebSocket │
│ новостная лента │ └──────────────┘
└────────────────────────┘

---

## ⚙️ Установка

### 📁 Клонируем репозиторий

```bash
lucky-jobgit clone https://github.com/yourname/lucky-job.git
cd lucky-job

🐳 Запуск через Docker

docker-compose up --build

docker-compose exec backend python manage.py createsuperuser


📂 Структура проекта

├── backend
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── lucky_job
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __pycache__
│   └── requirements.txt
├── fastapi_app
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── main.py
│   └── requirements.txt
├── frontend
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── nuxt.config.js
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   └── __pycache__
└── README.md

💬 WebSocket Endpoints

| Назначение      | Эндпоинт                                         |
| --------------- | ------------------------------------------------ |
| Чат             | `ws://localhost:8001/ws/chat/{user_id}`          |
| Уведомления     | `ws://localhost:8001/ws/notifications/{user_id}` |
| Новостная лента | `ws://localhost:8001/ws/news`                    |


🛠️ Возможности

-   🔍 Фильтрация вакансий и резюме

-   💬 Real-time чат между компаниями и кандидатами

-   🔔 Уведомления о новых сообщениях и событиях

-   📰 Лента новостей компаний

-   🔐 JWT аутентификация

-   📊 Панель администратора для компаний


📅 Roadmap
 Базовая система вакансий/резюме

 Аутентификация и роли пользователей

 Реализация WebSocket-чата

 Уведомления в реальном времени

 Подписка на компании / темы

 Мобильная адаптация

 Поддержка WebRTC для интервью
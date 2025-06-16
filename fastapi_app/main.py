from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-nuxt-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
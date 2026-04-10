from fastapi import FastAPI

from api.routes.leitores import router as leitor_router
from api.routes.livros import router as livro_router

app = FastAPI(title="API Biblioteca")

app.include_router(leitor_router)
app.include_router(livro_router)

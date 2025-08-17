from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Arabic Novel Archive",
    summary="Arabic Novel Archive",
    version="0.1.0",
)

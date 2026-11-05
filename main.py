from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="ML Inference DAG Gateway")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    # Start the API gateway
    uvicorn.run(app, host="0.0.0.0", port=8000)

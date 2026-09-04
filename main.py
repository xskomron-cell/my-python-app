from fastapi import FastAPI

app = FastAPI(title="Mening Python Loyiham")

@app.get("/")
def home():
    return {"status": "Aktiv", "message": "Xush kelibsiz! Loyiha muvaffaqiyatli ishlayapti."}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Mahsulot #{item_id}"}

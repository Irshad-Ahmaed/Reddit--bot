from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates
import uvicorn
from scheduler import start_scheduler
import threading
from pathlib import Path
from logger import logger

app = FastAPI()

# Create a threading Event
stop_event = threading.Event()

# Define the path to the templates directory 
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/start")
def start_bot():
    if not stop_event.is_set():
        thread = threading.Thread(target=start_scheduler, daemon=True)
        thread.start()
        logger.info("Scheduler started!")
        return {"message": "Scheduler started!"}
    return {"message": "Scheduler is already running!"}

@app.get("/stop")
def stop_bot(): 
    stop_event.set() # Set the event to stop the scheduler 
    logger.info("Scheduler stopped")
    return {"message": "Scheduler stopped!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

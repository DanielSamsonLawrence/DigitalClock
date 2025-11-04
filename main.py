from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_clock():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Digital Clock</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: black;
                color: lime;
                font-family: 'Courier New', monospace;
                font-size: 80px;
            }
            #clock {
                text-shadow: 0 0 10px lime;
            }
        </style>
    </head>
    <body>
        <div id="clock">00:00:00</div>

        <script>
            function updateClock() {
                const now = new Date();
                const hours = String(now.getHours()).padStart(2, '0');
                const minutes = String(now.getMinutes()).padStart(2, '0');
                const seconds = String(now.getSeconds()).padStart(2, '0');
                document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;
            }
            setInterval(updateClock, 1000);
            updateClock(); // initialize immediately
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
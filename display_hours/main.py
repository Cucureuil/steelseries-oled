import requests
import json
import time
from datetime import datetime

# url gamesens api
COREPROPS_PATH = "C:\\ProgramData\\SteelSeries\\SteelSeries Engine 3\\coreProps.json"

def register_event(core_url):
    payload = {
        "game": "CLOCK_APP",
        "event": "SHOW_TIME",
        "value_optional": True,
        "handlers": [
            {
                "device-type": "screened",
                "zone": "one",
                "mode": "screen",
                "datas": [
                    {"has-text": True, "arg": "value"}
                ]
            }
        ]
    }
    response = requests.post(f"{core_url}/bind_game_event", json=payload)
    print("Event registration response:", response.json())

def get_core_props():
    with open(COREPROPS_PATH, 'r') as file:
        core_props = json.load(file)
    return f"http://{core_props['address']}"

def register_app(core_url):
    payload = {
        "game": "CLOCK_APP",
        "game_display_name": "Clock",
        "developer": "random"
    }
    requests.post(f"{core_url}/game_metadata", json=payload)

def send_clock_event(core_url):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        payload = {
            "game": "CLOCK_APP",
            "event": "SHOW_TIME",
            "data": {
                "value": current_time
            }
        }
        response = requests.post(f"{core_url}/game_event", json=payload)
        print("Send event response:", response.json())
        time.sleep(10)

def main():
    core_url = get_core_props()
    register_app(core_url)
    register_event(core_url)
    send_clock_event(core_url)


if __name__ == "__main__":
    main()

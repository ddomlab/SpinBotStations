import os, requests
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
ELN_KEY = os.environ.get("ELN_API_KEY")
BASE_URL = "https://eln.ddomlab.org/api/v2"
HEADERS = {
    "Authorization": f"{ELN_KEY}",
    "Content-Type": "application/json"
}

class eln:
    def __init__(self, debug=False):
        self.title = None
        self.desc = None
        self.debug = debug
        self.id = None
        pass

    def init_experiment(self, title: str, desc: str):
        """Creates an experiment and then pushes it to the eln

        Args:
            title (str, optional): Title of experiment. If no title is provided, you will be prompted.
            desc (str, optional): Description of experiment. If not description is provided, you will be prompted.
            debug (bool, optional): If true, then no HTTP request will be sent to the server.

        Returns:
            int: ID of experiment just added
        """
        self.title = title
        self.desc = desc

        data = {
            "canwrite": "{\"base\":30,\"teams\":[],\"teamgroups\":[],\"users\":[]}",
            "title": title,
            "body": desc
        }

        r = requests.post(f"{BASE_URL}/experiments/", headers=HEADERS, json=data)
        if r.status_code != 201:
            raise RuntimeWarning(f"Error code: {r.status_code}\nCould not send this following data:\n{data}")

        self.id = int(r.headers["Location"][43:])
        return self.id
    
# if __name__ == "__main__":
#     e = eln(title="Testing", desc="This is a test", debug=True)
#     print(e.init_experiment())
#     print(e.title)
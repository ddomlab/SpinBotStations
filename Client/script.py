import os
from dotenv import load_dotenv
from SpinbotStations import imagestation

load_dotenv()

ex = eln(debug=True)
ex.init_experiment(title="Testing", desc="This is a test of the API I am working with")
print(ex.id)


# station_1 = imagestation(
#     pi_url='http://100.107.255.14:8080',
#     api_key=os.environ.get("API_KEY") # type: ignore
#     )

# img = station_1.capture(filename='testing')
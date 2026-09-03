import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
TARGET_URL = "https://api.trafikinfo.trafikverket.se/v2/data.json"
XML = f"""
<REQUEST>
  <LOGIN authenticationkey="{API_KEY}" />
  <QUERY objecttype="Camera" schemaversion="1" limit="20">
    <FILTER>
      <WITHIN name="Geometry.SWEREF99TM"
              shape="center"
              value="374608 6404476"
              radius="15000" />
    </FILTER>
  </QUERY>
</REQUEST>
"""
HEADER = {'Content-Type': 'application/xml'}
def main():
    print(XML)
    response = requests.post(TARGET_URL, data=XML.encode("utf-8"), headers=HEADER)
    print(response.status_code)
    print(response.text)

    #picture_url = "https://api.trafikinfo.trafikverket.se/v2/Images/data/road.infrastructure.camera/TrafficFlowCamera_39636104.jpg"
    #response_picture = requests.get(picture_url)
    #with open("test.jpg", "wb") as file:
    #    file.write(response_picture.content)





if __name__ == "__main__":
    main()
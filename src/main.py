import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
TARGET_URL = "https://api.trafikinfo.trafikverket.se/v2/data.json"
XML = f"""
<REQUEST>
  <LOGIN authenticationkey="{API_KEY}" />
  <QUERY objecttype="Camera" schemaversion="1" limit="5">
  </QUERY>
</REQUEST>
"""
HEADER = {'Content-Type': 'application/xml'}
def main():
    print(XML)
    response = requests.post(TARGET_URL, data=XML, headers=HEADER)
    print(response.status_code)
    print(response.text)






if __name__ == "__main__":
    main()
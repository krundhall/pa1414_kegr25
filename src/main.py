import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
TARGET_URL = "https://api.trafikinfo.trafikverket.se/v2/data.json"
XML = f"""
<REQUEST>
  <LOGIN authenticationkey="{API_KEY}" />
  <QUERY objecttype="Camera" schemaversion="1">
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
    response = requests.post(TARGET_URL, data=XML.encode("utf-8"), headers=HEADER)
    if response.status_code != 200:
        print(f"[ERROR] {response.status_code}: {response.text}")

    data = response.json()
    cameras = data["RESPONSE"]["RESULT"][0]["Camera"]
    filtered_cameras = []

    print(f"Found {len(cameras)} cameras near Borås:\n")
    for camera in cameras:

        camera_id = camera.get("Id")
        if camera_id.startswith("SE_STA_CAMERA_VViS_"):
            continue

        filtered_cameras.append(camera)

        name = camera.get("Name")
        location = camera.get("Location")
        photo_url = camera.get("PhotoUrl")
        direction = camera.get("Direction")

        print(f"ID: {camera_id}")
        print(f"Name: {name}")
        print(f"Location: {location}")
        print(f"Direction: {direction}°"
              if direction is not None
              else "Direction: Unknown")
        print(f"Image URL: {photo_url}")
        print("-" * 40)

    print(f"\nTotal filtered traffic cameras: {len(filtered_cameras)}")


    #picture_url = "https://api.trafikinfo.trafikverket.se/v2/Images/data/road.infrastructure.camera/TrafficFlowCamera_39636104.jpg"
    #response_picture = requests.get(picture_url)
    #with open("test.jpg", "wb") as file:
    #    file.write(response_picture.content)





if __name__ == "__main__":
    main()
from fastapi import APIRouter
from fastapi import Request
from fastapi import Response
from fastapi import HTTPException
import json
import xml.etree.cElementTree as Et

from models.geo_models import GeoLocationRequest
import requests

router = APIRouter()


@router.post(path="/getAddressDetails", tags=["Geo API"])
async def get_get_data(request: Request, data: GeoLocationRequest):
    # get configs
    key_val = await request.app.fetch_config("ACCESS_API_KEY")
    api_url = await request.app.fetch_config("API_URL")
    api_output = requests.get(
        api_url.format(**{"outputFormat": "json", "address": data.address.replace(" ", "+"), "key": key_val})
    )
    if api_output.status_code == 400:
        return HTTPException(status_code=422, detail="Invalid Address")
    # Extracting needed info for response
    results = api_output.json().get("results")[0]
    lat = results.get("geometry", "").get("location", "").get("lat", "")
    lng = results.get("geometry", "").get("location", "").get("lng", "")
    address = results.get("formatted_address")

    output = ""
    if data.output_format == "json":
        output = {"coordinates": {"lat": lat, "lng": lng}, "address": address}
        output = json.dumps(output)
    elif data.output_format == "xml":
        root = Et.Element("root")
        Et.SubElement(root, "address").text = address
        coordinates = Et.SubElement(root, "coordinates")
        Et.SubElement(coordinates, "lat").text = str(lat)
        Et.SubElement(coordinates, "lng").text = str(lng)
        output = Et.tostring(root, encoding="utf8", method="xml")

    media_type = f"application/{data.output_format}"
    return Response(content=output, media_type=media_type)

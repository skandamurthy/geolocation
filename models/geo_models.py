from pydantic import BaseModel
from pydantic import Field
from typing import Literal

OUTPUT_FORMATS = Literal["json", "xml"]


class GeoLocationRequest(BaseModel):
    """
    Request model for the Gro Location API
    """

    address: str = Field(description="Address request field", default="")
    output_format: str = Field(description="Output format requested", default="json")

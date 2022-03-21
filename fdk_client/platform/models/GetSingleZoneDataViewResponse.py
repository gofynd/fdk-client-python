"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetZoneDataViewItems import GetZoneDataViewItems


class GetSingleZoneDataViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.List(fields.Nested(GetZoneDataViewItems, required=False), required=False)
    


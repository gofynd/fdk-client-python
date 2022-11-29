"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ZoneDataItem import ZoneDataItem

from .ListViewItems import ListViewItems


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


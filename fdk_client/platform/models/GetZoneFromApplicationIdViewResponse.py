"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ListViewItems import ListViewItems

from .ZoneDataItem import ZoneDataItem


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    


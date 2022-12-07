"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ListViewSummary import ListViewSummary

from .ZoneDataItem import ZoneDataItem

from .ListViewItems import ListViewItems


class ListViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PointsHistory import PointsHistory

from .Page import Page




class HistoryRes(BaseSchema):
    # Rewards swagger.json

    
    items = fields.List(fields.Nested(PointsHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    points = fields.Float(required=False)
    


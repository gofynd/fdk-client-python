"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Page import Page




class GetEngineResponse(BaseSchema):
    # Finance swagger.json

    
    item_count = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    


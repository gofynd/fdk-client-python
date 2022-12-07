"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ItemCriterias(BaseSchema):
    # Orders swagger.json

    
    item_brand = fields.List(fields.Int(required=False), required=False)
    


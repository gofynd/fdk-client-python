"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Dates(BaseSchema):
    # Order swagger.json

    
    delivery_date = fields.Raw(required=False)
    
    order_created = fields.Str(required=False)
    


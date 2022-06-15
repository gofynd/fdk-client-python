"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CollectionPrice(BaseSchema):
    # Catalog swagger.json

    
    lte = fields.Int(required=False)
    
    gte = fields.Int(required=False)
    


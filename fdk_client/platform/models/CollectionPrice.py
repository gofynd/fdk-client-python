"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CollectionPrice(BaseSchema):
    # Catalog swagger.json

    
    gte = fields.Int(required=False)
    
    lte = fields.Int(required=False)
    


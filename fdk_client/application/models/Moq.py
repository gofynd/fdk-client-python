"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Moq(BaseSchema):
    # Catalog swagger.json

    
    minimum = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    


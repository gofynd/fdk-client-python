"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class MOQData(BaseSchema):
    # Catalog swagger.json

    
    minimum = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    


"""Logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ListViewProduct(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    count = fields.Int(required=False)
    

"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Time(BaseSchema):
    #  swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    

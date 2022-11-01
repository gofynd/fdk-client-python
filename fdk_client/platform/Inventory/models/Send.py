"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Send(BaseSchema):
    #  swagger.json

    
    raw = fields.Boolean(required=False)
    
    processed = fields.Boolean(required=False)
    

"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Meta import Meta







class Media(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    url = fields.Str(required=False)
    
    alt = fields.Str(required=False)
    

"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .Meta import Meta



class Media(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    

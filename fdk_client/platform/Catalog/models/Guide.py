"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Meta import Meta



class Guide(BaseSchema):
    #  swagger.json

    
    meta = fields.Nested(Meta, required=False)
    

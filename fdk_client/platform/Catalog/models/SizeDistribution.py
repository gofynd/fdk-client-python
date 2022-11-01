"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SetSize import SetSize



class SizeDistribution(BaseSchema):
    #  swagger.json

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    

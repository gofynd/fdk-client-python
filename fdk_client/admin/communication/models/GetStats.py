"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Stats import Stats



class GetStats(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Stats, required=False), required=False)
    

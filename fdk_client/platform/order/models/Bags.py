"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BagItem import BagItem





class Bags(BaseSchema):
    #  swagger.json

    
    item = fields.Nested(BagItem, required=False)
    
    id = fields.Int(required=False)
    

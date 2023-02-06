"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FilerList import FilerList





class InventoryConfig(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(FilerList, required=False), required=False)
    
    multivalues = fields.Boolean(required=False)
    

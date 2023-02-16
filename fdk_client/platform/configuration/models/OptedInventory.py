"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OptType import OptType





class OptedInventory(BaseSchema):
    #  swagger.json

    
    opt_type = fields.Nested(OptType, required=False)
    
    items = fields.Raw(required=False)
    

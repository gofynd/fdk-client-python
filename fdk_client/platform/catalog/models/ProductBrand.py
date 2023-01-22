"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Media1 import Media1





from .Action import Action





class ProductBrand(BaseSchema):
    #  swagger.json

    
    logo = fields.Nested(Media1, required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    

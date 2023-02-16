"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ItemBrand(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

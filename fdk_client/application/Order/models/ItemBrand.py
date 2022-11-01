"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ItemBrand(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

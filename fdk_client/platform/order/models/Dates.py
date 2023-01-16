"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Dates(BaseSchema):
    #  swagger.json

    
    delivery_date = fields.Raw(required=False)
    
    order_created = fields.Str(required=False)
    

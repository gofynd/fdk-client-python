"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Dates(BaseSchema):
    #  swagger.json

    
    order_created = fields.Str(required=False)
    
    delivery_date = fields.Raw(required=False)
    

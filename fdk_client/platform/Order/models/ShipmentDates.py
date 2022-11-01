"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ShipmentDates(BaseSchema):
    #  swagger.json

    
    due_date = fields.Str(required=False)
    

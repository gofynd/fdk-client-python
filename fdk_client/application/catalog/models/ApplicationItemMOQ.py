"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ApplicationItemMOQ(BaseSchema):
    #  swagger.json

    
    minimum = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    

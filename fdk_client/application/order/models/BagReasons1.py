"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class BagReasons1(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    

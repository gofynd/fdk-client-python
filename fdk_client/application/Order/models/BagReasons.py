"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class BagReasons(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

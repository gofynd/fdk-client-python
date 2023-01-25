"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ShipmentsRequest import ShipmentsRequest



class StatuesRequest(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentsRequest, required=False), required=False)
    

"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class OriginalFilter(BaseSchema):
    #  swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    

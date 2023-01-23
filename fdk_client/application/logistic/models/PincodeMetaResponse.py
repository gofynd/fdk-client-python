"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PincodeMetaResponse(BaseSchema):
    #  swagger.json

    
    zone = fields.Str(required=False)
    
    internal_zone_id = fields.Int(required=False)
    

"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetPincodeZonesResponse(BaseSchema):
    #  swagger.json

    
    zones = fields.List(fields.Raw(required=False), required=False)
    
    serviceability_type = fields.Str(required=False)
    

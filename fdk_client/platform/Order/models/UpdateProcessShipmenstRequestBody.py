"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UpdateProcessShipmenstRequestBody(BaseSchema):
    #  swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    expected_status = fields.Str(required=False)
    

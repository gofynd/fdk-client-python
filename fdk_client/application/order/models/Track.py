"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




















class Track(BaseSchema):
    #  swagger.json

    
    last_location_recieved_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    account_name = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    

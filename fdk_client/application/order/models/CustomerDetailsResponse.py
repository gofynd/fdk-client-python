"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class CustomerDetailsResponse(BaseSchema):
    #  swagger.json

    
    phone = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    

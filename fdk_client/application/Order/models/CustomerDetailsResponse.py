"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class CustomerDetailsResponse(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
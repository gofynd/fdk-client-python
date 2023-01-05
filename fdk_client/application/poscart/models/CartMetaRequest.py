"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class CartMetaRequest(BaseSchema):
    #  swagger.json

    
    comment = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    checkout_mode = fields.Str(required=False)
    

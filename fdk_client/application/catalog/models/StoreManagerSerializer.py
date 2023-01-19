"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .SellerPhoneNumber import SellerPhoneNumber



class StoreManagerSerializer(BaseSchema):
    #  swagger.json

    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    

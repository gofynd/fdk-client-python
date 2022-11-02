"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class SellerPhoneNumber(BaseSchema):
    #  swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    

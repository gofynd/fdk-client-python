"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class StrategyWiseListingSchemaV2(BaseSchema):
    #  swagger.json

    
    distance = fields.Int(required=False)
    
    pincode = fields.Int(required=False)
    
    tat = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    

"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ReturnConfigSchemaV2(BaseSchema):
    #  swagger.json

    
    time = fields.Int(required=False)
    
    returnable = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    

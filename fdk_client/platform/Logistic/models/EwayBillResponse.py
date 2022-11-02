"""Logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class EwayBillResponse(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    

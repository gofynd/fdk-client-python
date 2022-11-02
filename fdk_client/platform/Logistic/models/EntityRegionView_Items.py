"""Logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class EntityRegionView_Items(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    

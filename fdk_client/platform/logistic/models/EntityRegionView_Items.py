"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class EntityRegionView_Items(BaseSchema):
    #  swagger.json

    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    

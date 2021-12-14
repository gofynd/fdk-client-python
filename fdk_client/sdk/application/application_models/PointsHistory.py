"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






























class PointsHistory(BaseSchema):
    # Rewards swagger.json

    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    claimed = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    points = fields.Float(required=False)
    
    remaining_points = fields.Float(required=False)
    
    text_1 = fields.Str(required=False)
    
    text_2 = fields.Str(required=False)
    
    text_3 = fields.Str(required=False)
    
    txn_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class SearchLogReq(BaseSchema):
    #  swagger.json

    
    marketplace_name = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    identifier_value = fields.Str(required=False)
    

"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class MerchantOnBoardingRequest(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    credit_line_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


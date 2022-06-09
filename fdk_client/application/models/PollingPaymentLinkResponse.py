"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PollingPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    http_status = fields.Int(required=False)
    


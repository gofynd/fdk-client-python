"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .PendingAcceptance import PendingAcceptance


class MetricsCount(BaseSchema):
    # Orders swagger.json

    
    pending_rtd = fields.Int(required=False)
    
    cancelled = fields.Int(required=False)
    
    returned = fields.Int(required=False)
    
    pending_pickup = fields.Int(required=False)
    
    pending_acceptance = fields.List(fields.Nested(PendingAcceptance, required=False), required=False)
    


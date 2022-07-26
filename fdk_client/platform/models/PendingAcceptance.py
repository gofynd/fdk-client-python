"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PendingAcceptance(BaseSchema):
    # Orders swagger.json

    
    cod = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    prepaid = fields.Int(required=False)
    


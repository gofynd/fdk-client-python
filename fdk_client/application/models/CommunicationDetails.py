"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CommunicationDetails(BaseSchema):
    # Lead swagger.json

    
    type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


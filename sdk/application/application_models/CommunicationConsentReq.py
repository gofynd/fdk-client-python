"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class CommunicationConsentReq(BaseSchema):

    
    response = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    


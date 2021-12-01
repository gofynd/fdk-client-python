"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class CommunicationConsentChannelsEmail(BaseSchema):

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .CommunicationConsentChannels import CommunicationConsentChannels


class CommunicationConsentRes(BaseSchema):
    # Communication swagger.json

    
    app_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    channels = fields.Nested(CommunicationConsentChannels, required=False)
    


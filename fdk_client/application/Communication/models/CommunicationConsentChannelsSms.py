"""Communication Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CommunicationConsentChannelsSms(BaseSchema):
    #  swagger.json

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

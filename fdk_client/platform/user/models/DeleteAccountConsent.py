"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DeleteAccountConsent(BaseSchema):
    #  swagger.json

    
    consent_text = fields.Str(required=False)
    

"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class DeleteAccountConsent(BaseSchema):
    #  swagger.json

    
    consent_text = fields.Str(required=False)
    

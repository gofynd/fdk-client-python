"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UploadConsent(BaseSchema):
    #  swagger.json

    
    consent_url = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    

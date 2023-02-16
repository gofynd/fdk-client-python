"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DispatchManifest(BaseSchema):
    #  swagger.json

    
    manifest_id = fields.Str(required=False)
    

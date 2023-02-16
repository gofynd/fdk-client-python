"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OneTimeChargeEntity import OneTimeChargeEntity





class CreateOneTimeChargeResponse(BaseSchema):
    #  swagger.json

    
    charge = fields.Nested(OneTimeChargeEntity, required=False)
    
    confirm_url = fields.Str(required=False)
    

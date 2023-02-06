"""inventory Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema








class ApikeyModel(BaseSchema):
    #  swagger.json

    
    session_id = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    

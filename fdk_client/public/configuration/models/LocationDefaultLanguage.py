"""configuration Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema








class LocationDefaultLanguage(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

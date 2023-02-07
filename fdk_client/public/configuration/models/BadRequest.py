"""configuration Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema






class BadRequest(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    

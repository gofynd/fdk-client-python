"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class CreateUserSessionResponseSchema(BaseSchema):
    #  swagger.json

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    secure = fields.Boolean(required=False)
    
    http_only = fields.Boolean(required=False)
    
    cookie = fields.Dict(required=False)
    

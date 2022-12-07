"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class Document(BaseSchema):
    #  swagger.json

    
    verified = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
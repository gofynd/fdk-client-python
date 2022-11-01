"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UpdateDomain import UpdateDomain





class UpdateDomainTypeRequest(BaseSchema):
    #  swagger.json

    
    domain = fields.Nested(UpdateDomain, required=False)
    
    action = fields.Str(required=False)
    

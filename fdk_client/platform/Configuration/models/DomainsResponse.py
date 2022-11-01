"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Domain import Domain



class DomainsResponse(BaseSchema):
    #  swagger.json

    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    

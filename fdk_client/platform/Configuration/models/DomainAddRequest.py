"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DomainAdd import DomainAdd



class DomainAddRequest(BaseSchema):
    #  swagger.json

    
    domain = fields.Nested(DomainAdd, required=False)
    

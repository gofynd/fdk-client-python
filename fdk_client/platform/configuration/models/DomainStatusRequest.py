"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DomainStatusRequest(BaseSchema):
    #  swagger.json

    
    domain_url = fields.Str(required=False)
    

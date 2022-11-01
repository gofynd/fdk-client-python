"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GtmCredentials import GtmCredentials





class Gtm(BaseSchema):
    #  swagger.json

    
    credentials = fields.Nested(GtmCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    

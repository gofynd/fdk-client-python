"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class Document(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

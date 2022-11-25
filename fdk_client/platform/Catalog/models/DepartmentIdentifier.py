"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DepartmentIdentifier(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    

"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AttributeMasterDetails(BaseSchema):
    #  swagger.json

    
    display_type = fields.Str(required=False)
    

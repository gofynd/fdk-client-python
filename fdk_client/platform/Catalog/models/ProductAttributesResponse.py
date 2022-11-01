"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AttributeMasterSerializer import AttributeMasterSerializer



class ProductAttributesResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(AttributeMasterSerializer, required=False), required=False)
    

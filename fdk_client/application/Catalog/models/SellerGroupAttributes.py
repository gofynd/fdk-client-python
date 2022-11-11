"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .DetailsSchemaV2 import DetailsSchemaV2



class SellerGroupAttributes(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(DetailsSchemaV2, required=False), required=False)
    

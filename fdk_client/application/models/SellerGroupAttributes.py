"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DetailsSchemaV3 import DetailsSchemaV3


class SellerGroupAttributes(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(DetailsSchemaV3, required=False), required=False)
    


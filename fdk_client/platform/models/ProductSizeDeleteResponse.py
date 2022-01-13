"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductSizeDeleteDataResponse import ProductSizeDeleteDataResponse


class ProductSizeDeleteResponse(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ProductSizeDeleteDataResponse, required=False)
    

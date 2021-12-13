"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ProductSizeDeleteDataResponse import ProductSizeDeleteDataResponse


class ProductSizeDeleteResponse(BaseSchema):

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ProductSizeDeleteDataResponse, required=False)
    


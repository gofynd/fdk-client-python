"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .SEOData import SEOData

from .MOQData import MOQData


class OwnerAppItemResponse(BaseSchema):
    # Catalog swagger.json

    
    is_gift = fields.Boolean(required=False)
    
    alt_text = fields.Dict(required=False)
    
    is_cod = fields.Boolean(required=False)
    
    seo = fields.Nested(SEOData, required=False)
    
    moq = fields.Nested(MOQData, required=False)
    

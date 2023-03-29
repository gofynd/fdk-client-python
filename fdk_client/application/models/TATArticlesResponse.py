"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATErrorSchemaResponse import TATErrorSchemaResponse





from .TATCategoryRequest import TATCategoryRequest





from .TATPromiseResponse import TATPromiseResponse


class TATArticlesResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    


"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .TATCategoryRequest import TATCategoryRequest





from .TATErrorSchemaResponse import TATErrorSchemaResponse



from .TATPromiseResponse import TATPromiseResponse


class TATArticlesResponse(BaseSchema):
    # Logistic swagger.json

    
    manufacturing_time = fields.Int(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    


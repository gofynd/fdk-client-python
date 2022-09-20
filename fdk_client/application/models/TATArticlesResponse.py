"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATPromiseResponse import TATPromiseResponse





from .TATCategoryRequest import TATCategoryRequest



from .TATErrorSchemaResponse import TATErrorSchemaResponse




class TATArticlesResponse(BaseSchema):
    # Logistic swagger.json

    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    _manufacturing_time_seconds = fields.Str(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    


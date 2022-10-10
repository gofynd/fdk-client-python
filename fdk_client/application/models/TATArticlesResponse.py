"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATCategoryRequest import TATCategoryRequest

from .TATPromiseResponse import TATPromiseResponse







from .TATErrorSchemaResponse import TATErrorSchemaResponse




class TATArticlesResponse(BaseSchema):
    # Logistic swagger.json

    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    

"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TATCategoryRequest import TATCategoryRequest







from .TATPromiseResponse import TATPromiseResponse





from .TATErrorSchemaResponse import TATErrorSchemaResponse





class TATArticlesResponse(BaseSchema):
    #  swagger.json

    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    

"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .TATCategoryRequest import TATCategoryRequest







from .TATErrorSchemaResponse import TATErrorSchemaResponse



from .TATPromiseResponse import TATPromiseResponse





class TATArticlesResponse(BaseSchema):
    #  swagger.json

    
    _manufacturing_time_seconds = fields.Int(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    

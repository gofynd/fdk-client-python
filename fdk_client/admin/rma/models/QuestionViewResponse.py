"""rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ItemsData import ItemsData



from .ErrorData import ErrorData





from .PageData import PageData



class QuestionViewResponse(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(ItemsData, required=False)
    
    error = fields.Nested(ErrorData, required=False)
    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(PageData, required=False)
    

"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OpeningClosing import OpeningClosing







from .OpeningClosing import OpeningClosing



class TimmingResponse(BaseSchema):
    #  swagger.json

    
    closing = fields.Nested(OpeningClosing, required=False)
    
    open = fields.Boolean(required=False)
    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(OpeningClosing, required=False)
    

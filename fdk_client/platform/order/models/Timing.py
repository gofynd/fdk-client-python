"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Opening import Opening







from .Closing import Closing



class Timing(BaseSchema):
    #  swagger.json

    
    opening = fields.Nested(Opening, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(Closing, required=False)
    

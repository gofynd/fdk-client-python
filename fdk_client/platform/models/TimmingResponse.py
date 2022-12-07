"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OpeningClosing import OpeningClosing

from .OpeningClosing import OpeningClosing




class TimmingResponse(BaseSchema):
    # Serviceability swagger.json

    
    open = fields.Boolean(required=False)
    
    opening = fields.Nested(OpeningClosing, required=False)
    
    closing = fields.Nested(OpeningClosing, required=False)
    
    weekday = fields.Str(required=False)
    


"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LandingPageSchema import LandingPageSchema





class LandingPage(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(LandingPageSchema, required=False)
    
    success = fields.Boolean(required=False)
    

"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Gst import Gst



class Documents(BaseSchema):
    #  swagger.json

    
    gst = fields.Nested(Gst, required=False)
    

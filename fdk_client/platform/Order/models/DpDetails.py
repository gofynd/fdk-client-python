"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DpDetails(BaseSchema):
    #  swagger.json

    
    gst_tag = fields.Str(required=False)
    

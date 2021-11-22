"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Images import Images








class Information(Schema):

    
    images = fields.Nested(Images, required=False)
    
    features = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


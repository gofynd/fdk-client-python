"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AllSizes import AllSizes



class ListALLSizes(BaseSchema):
    #  swagger.json

    
    all_sizes = fields.List(fields.Nested(AllSizes, required=False), required=False)
    

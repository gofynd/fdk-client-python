"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ALLSizes import ALLSizes



class ListALLSizes(BaseSchema):
    #  swagger.json

    
    all_sizes = fields.List(fields.Nested(ALLSizes, required=False), required=False)
    

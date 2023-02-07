"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .HsnCodesObject import HsnCodesObject



class HsnCode(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(HsnCodesObject, required=False)
    

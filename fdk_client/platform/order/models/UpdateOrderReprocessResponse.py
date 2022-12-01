"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class UpdateOrderReprocessResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    

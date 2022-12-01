"""rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ReasonListViewResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Str(required=False)
    

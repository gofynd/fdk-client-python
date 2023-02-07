"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Dp import Dp





class LogisticsResponse(BaseSchema):
    #  swagger.json

    
    dp = fields.Nested(Dp, required=False)
    
    override = fields.Boolean(required=False)
    

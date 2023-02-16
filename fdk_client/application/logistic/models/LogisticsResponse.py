"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class LogisticsResponse(BaseSchema):
    #  swagger.json

    
    dp = fields.Dict(required=False)
    

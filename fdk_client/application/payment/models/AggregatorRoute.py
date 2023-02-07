"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class AggregatorRoute(BaseSchema):
    #  swagger.json

    
    payment_flow = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    payment_flow_data = fields.Str(required=False)
    
    api_link = fields.Str(required=False)
    

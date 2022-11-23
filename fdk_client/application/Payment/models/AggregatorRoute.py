"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class AggregatorRoute(BaseSchema):
    #  swagger.json

    
    api_link = fields.Str(required=False)
    
    payment_flow = fields.Str(required=False)
    
    payment_flow_data = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    

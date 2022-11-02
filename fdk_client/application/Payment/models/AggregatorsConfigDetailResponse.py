"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AggregatorConfigDetail import AggregatorConfigDetail



from .AggregatorConfigDetail import AggregatorConfigDetail



from .AggregatorConfigDetail import AggregatorConfigDetail



from .AggregatorConfigDetail import AggregatorConfigDetail



from .AggregatorConfigDetail import AggregatorConfigDetail



from .AggregatorConfigDetail import AggregatorConfigDetail





from .AggregatorConfigDetail import AggregatorConfigDetail





from .AggregatorConfigDetail import AggregatorConfigDetail



class AggregatorsConfigDetailResponse(BaseSchema):
    #  swagger.json

    
    stripe = fields.Nested(AggregatorConfigDetail, required=False)
    
    mswipe = fields.Nested(AggregatorConfigDetail, required=False)
    
    razorpay = fields.Nested(AggregatorConfigDetail, required=False)
    
    payumoney = fields.Nested(AggregatorConfigDetail, required=False)
    
    ccavenue = fields.Nested(AggregatorConfigDetail, required=False)
    
    simpl = fields.Nested(AggregatorConfigDetail, required=False)
    
    success = fields.Boolean(required=False)
    
    rupifi = fields.Nested(AggregatorConfigDetail, required=False)
    
    env = fields.Str(required=False)
    
    juspay = fields.Nested(AggregatorConfigDetail, required=False)
    
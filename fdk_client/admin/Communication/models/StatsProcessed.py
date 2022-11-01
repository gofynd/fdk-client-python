"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StatsProcessedEmail import StatsProcessedEmail



from .StatsProcessedSms import StatsProcessedSms



class StatsProcessed(BaseSchema):
    #  swagger.json

    
    email = fields.Nested(StatsProcessedEmail, required=False)
    
    sms = fields.Nested(StatsProcessedSms, required=False)
    

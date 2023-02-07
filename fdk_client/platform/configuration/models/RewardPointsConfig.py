"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Credit import Credit



from .Debit import Debit



class RewardPointsConfig(BaseSchema):
    #  swagger.json

    
    credit = fields.Nested(Credit, required=False)
    
    debit = fields.Nested(Debit, required=False)
    

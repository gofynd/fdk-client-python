"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class RewardPointRequest(BaseSchema):
    #  swagger.json

    
    points = fields.Boolean(required=False)
    

"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class FyndRewardsCredentials(BaseSchema):
    #  swagger.json

    
    public_key = fields.Str(required=False)
    

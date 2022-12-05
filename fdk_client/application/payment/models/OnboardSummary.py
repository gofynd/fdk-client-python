"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class OnboardSummary(BaseSchema):
    #  swagger.json

    
    status = fields.Boolean(required=False)
    
    session = fields.Dict(required=False)
    
    redirect_url = fields.Str(required=False)
    

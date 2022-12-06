"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class FeedbackForm(BaseSchema):
    #  swagger.json

    
    inputs = fields.Dict(required=False)
    
    title = fields.Str(required=False)
    
    timestamps = fields.Dict(required=False)
    

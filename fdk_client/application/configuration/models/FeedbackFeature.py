"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class FeedbackFeature(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    

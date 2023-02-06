"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class FAQ(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    

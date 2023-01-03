"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CreditDetail(BaseSchema):
    #  swagger.json

    
    status = fields.Boolean(required=False)
    
    is_registered = fields.Boolean(required=False)
    
    signup_url = fields.Str(required=False)
    

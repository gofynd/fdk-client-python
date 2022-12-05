"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CreditDetail(BaseSchema):
    #  swagger.json

    
    is_registered = fields.Boolean(required=False)
    
    signup_url = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    

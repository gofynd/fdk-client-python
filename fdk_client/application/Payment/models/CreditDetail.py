"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CreditDetail(BaseSchema):
    #  swagger.json

    
    signup_url = fields.Str(required=False)
    
    is_registered = fields.Boolean(required=False)
    
    status = fields.Boolean(required=False)
    

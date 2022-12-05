"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class RedirectURL(BaseSchema):
    #  swagger.json

    
    signup_url = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    

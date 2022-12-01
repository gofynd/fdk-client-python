"""share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class Attribution(BaseSchema):
    #  swagger.json

    
    campaign_cookie_expiry = fields.Str(required=False)
    

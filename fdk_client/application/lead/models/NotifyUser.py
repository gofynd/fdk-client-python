"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class NotifyUser(BaseSchema):
    #  swagger.json

    
    country_code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    

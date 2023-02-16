"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CreatedOn(BaseSchema):
    #  swagger.json

    
    user_agent = fields.Str(required=False)
    

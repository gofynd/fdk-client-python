"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class UserDetail(BaseSchema):
    #  swagger.json

    
    contact = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    super_user = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
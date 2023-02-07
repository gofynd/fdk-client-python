"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class Social(BaseSchema):
    #  swagger.json

    
    account_kit = fields.Boolean(required=False)
    
    facebook = fields.Boolean(required=False)
    
    google = fields.Boolean(required=False)
    
    apple = fields.Boolean(required=False)
    

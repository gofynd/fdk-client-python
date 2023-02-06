"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class DeleteUserSuccess(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    

"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class SessionListSuccess(BaseSchema):
    #  swagger.json

    
    sessions = fields.List(fields.Str(required=False), required=False)
    

"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ApplicationVersionRequest(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    version = fields.Str(required=False)
    

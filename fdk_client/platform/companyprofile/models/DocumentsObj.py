"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DocumentsObj(BaseSchema):
    #  swagger.json

    
    pending = fields.Int(required=False)
    
    verified = fields.Int(required=False)
    

"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DocumentsObj(BaseSchema):
    #  swagger.json

    
    verified = fields.Int(required=False)
    
    pending = fields.Int(required=False)
    

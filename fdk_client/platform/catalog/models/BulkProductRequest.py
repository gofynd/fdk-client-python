"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class BulkProductRequest(BaseSchema):
    #  swagger.json

    
    template_tag = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    batch_id = fields.Str(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    

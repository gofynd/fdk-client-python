"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class BulkProductRequest(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    

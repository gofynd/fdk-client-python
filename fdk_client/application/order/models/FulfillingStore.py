"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class FulfillingStore(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    

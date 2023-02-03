"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from ._AssignStoreArticle import _AssignStoreArticle















class AssignStoreRequestValidator(BaseSchema):
    #  swagger.json

    
    articles = fields.List(fields.Nested(_AssignStoreArticle, required=False), required=False)
    
    channel_type = fields.Str(required=False)
    
    channel_identifier = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    

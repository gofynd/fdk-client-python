"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






















class AssignStoreRequest(BaseSchema):
    #  swagger.json

    
    extension_config = fields.Dict(required=False)
    
    page_no = fields.Int(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    application_config = fields.Dict(required=False)
    
    to_pincode = fields.Str(required=False)
    
    page_size = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    items = fields.Dict(required=False)
    
    customer_details = fields.Dict(required=False)
    

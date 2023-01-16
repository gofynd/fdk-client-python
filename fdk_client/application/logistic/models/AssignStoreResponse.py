"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






























class AssignStoreResponse(BaseSchema):
    #  swagger.json

    
    page_size = fields.Int(required=False)
    
    items = fields.Dict(required=False)
    
    error = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    page_no = fields.Int(required=False)
    
    company = fields.Dict(required=False)
    
    article = fields.Dict(required=False)
    
    store = fields.Dict(required=False)
    
    customer_details = fields.Dict(required=False)
    
    to_pincode = fields.Str(required=False)
    
    pystormbreaker_uuid = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    assigned_stores = fields.List(fields.Dict(required=False), required=False)
    

"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .IntegrationTypeResponse import IntegrationTypeResponse



from .WarningsResponse import WarningsResponse



from .DocumentsResponse import DocumentsResponse





from .TimmingResponse import TimmingResponse









from .CreatedByResponse import CreatedByResponse





from .ModifiedByResponse import ModifiedByResponse



from .ManagerResponse import ManagerResponse





from .ContactNumberResponse import ContactNumberResponse





from .AddressResponse import AddressResponse



from .GstCredentialsResponse import GstCredentialsResponse









from .LogisticsResponse import LogisticsResponse





from .ModifiedByResponse import ModifiedByResponse









from .ProductReturnConfigResponse import ProductReturnConfigResponse



class ItemResponse(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    _cls = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    

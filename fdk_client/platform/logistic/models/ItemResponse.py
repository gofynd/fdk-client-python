"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .GstCredentialsResponse import GstCredentialsResponse



from .ModifiedByResponse import ModifiedByResponse



from .IntegrationTypeResponse import IntegrationTypeResponse



from .AddressResponse import AddressResponse



from .ModifiedByResponse import ModifiedByResponse





from .ManagerResponse import ManagerResponse





from .DocumentsResponse import DocumentsResponse



from .LogisticsResponse import LogisticsResponse









from .TimmingResponse import TimmingResponse



from .ContactNumberResponse import ContactNumberResponse





from .ProductReturnConfigResponse import ProductReturnConfigResponse







from .CreatedByResponse import CreatedByResponse









from .WarningsResponse import WarningsResponse





class ItemResponse(BaseSchema):
    #  swagger.json

    
    verified_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company = fields.Int(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    created_on = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    _cls = fields.Str(required=False)
    

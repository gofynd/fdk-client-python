"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ProductReturnConfigResponse import ProductReturnConfigResponse







from .TimmingResponse import TimmingResponse



from .ModifiedByResponse import ModifiedByResponse



from .DocumentsResponse import DocumentsResponse





from .ManagerResponse import ManagerResponse



from .ModifiedByResponse import ModifiedByResponse



from .LogisticsResponse import LogisticsResponse







from .GstCredentialsResponse import GstCredentialsResponse



from .AddressResponse import AddressResponse







from .IntegrationTypeResponse import IntegrationTypeResponse



from .ContactNumberResponse import ContactNumberResponse



from .WarningsResponse import WarningsResponse





from .CreatedByResponse import CreatedByResponse















class ItemResponse(BaseSchema):
    #  swagger.json

    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    sub_type = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    _cls = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    code = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    stage = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    store_type = fields.Str(required=False)
    

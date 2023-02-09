"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ManagerResponse import ManagerResponse









from .ModifiedByResponse import ModifiedByResponse











from .ContactNumberResponse import ContactNumberResponse







from .ProductReturnConfigResponse import ProductReturnConfigResponse





from .TimmingResponse import TimmingResponse



from .AddressResponse import AddressResponse





from .LogisticsResponse import LogisticsResponse



from .ModifiedByResponse import ModifiedByResponse



from .WarningsResponse import WarningsResponse



from .CreatedByResponse import CreatedByResponse



from .GstCredentialsResponse import GstCredentialsResponse





from .IntegrationTypeResponse import IntegrationTypeResponse





from .DocumentsResponse import DocumentsResponse



class ItemResponse(BaseSchema):
    #  swagger.json

    
    stage = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company = fields.Int(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    sub_type = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    store_type = fields.Str(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    _cls = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    

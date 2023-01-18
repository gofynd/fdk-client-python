"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TimmingResponse import TimmingResponse







from .IntegrationTypeResponse import IntegrationTypeResponse



from .LogisticsResponse import LogisticsResponse





from .ModifiedByResponse import ModifiedByResponse



from .AddressResponse import AddressResponse





from .DocumentsResponse import DocumentsResponse



from .ManagerResponse import ManagerResponse



from .GstCredentialsResponse import GstCredentialsResponse















from .ContactNumberResponse import ContactNumberResponse



from .CreatedByResponse import CreatedByResponse



from .ProductReturnConfigResponse import ProductReturnConfigResponse











from .ModifiedByResponse import ModifiedByResponse



from .WarningsResponse import WarningsResponse





class ItemResponse(BaseSchema):
    #  swagger.json

    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    store_type = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    company = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    company_id = fields.Int(required=False)
    

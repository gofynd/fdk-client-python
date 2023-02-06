"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ManagerResponse import ManagerResponse











from .TimmingResponse import TimmingResponse





from .AddressResponse import AddressResponse



from .IntegrationTypeResponse import IntegrationTypeResponse













from .WarningsResponse import WarningsResponse



from .ProductReturnConfigResponse import ProductReturnConfigResponse



from .ContactNumberResponse import ContactNumberResponse



from .LogisticsResponse import LogisticsResponse





from .DocumentsResponse import DocumentsResponse







from .GstCredentialsResponse import GstCredentialsResponse



from .ModifiedByResponse import ModifiedByResponse





from .CreatedByResponse import CreatedByResponse





from .ModifiedByResponse import ModifiedByResponse



class ItemResponse(BaseSchema):
    #  swagger.json

    
    manager = fields.Nested(ManagerResponse, required=False)
    
    modified_on = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    _cls = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    stage = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    name = fields.Str(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    

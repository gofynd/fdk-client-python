"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductReturnConfigResponse import ProductReturnConfigResponse



from .AddressResponse import AddressResponse



from .GstCredentialsResponse import GstCredentialsResponse









from .ModifiedByResponse import ModifiedByResponse



from .ManagerResponse import ManagerResponse







from .IntegrationTypeResponse import IntegrationTypeResponse



from .TimmingResponse import TimmingResponse



from .LogisticsResponse import LogisticsResponse



from .ModifiedByResponse import ModifiedByResponse









from .DocumentsResponse import DocumentsResponse



from .CreatedByResponse import CreatedByResponse









from .ContactNumberResponse import ContactNumberResponse











from .WarningsResponse import WarningsResponse



class ItemResponse(BaseSchema):
    #  swagger.json

    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    created_on = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    sub_type = fields.Str(required=False)
    
    _cls = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    

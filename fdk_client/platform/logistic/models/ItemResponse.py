"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GstCredentialsResponse import GstCredentialsResponse











from .TimmingResponse import TimmingResponse



from .AddressResponse import AddressResponse







from .CreatedByResponse import CreatedByResponse



from .ModifiedByResponse import ModifiedByResponse





from .DocumentsResponse import DocumentsResponse





from .ContactNumberResponse import ContactNumberResponse





from .ModifiedByResponse import ModifiedByResponse











from .ManagerResponse import ManagerResponse



from .WarningsResponse import WarningsResponse



from .LogisticsResponse import LogisticsResponse







from .IntegrationTypeResponse import IntegrationTypeResponse



from .ProductReturnConfigResponse import ProductReturnConfigResponse



class ItemResponse(BaseSchema):
    #  swagger.json

    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    modified_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    code = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    _cls = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    company = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    sub_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    

"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .TimmingResponse import TimmingResponse







from .ModifiedByResponse import ModifiedByResponse



from .AddressResponse import AddressResponse



from .CreatedByResponse import CreatedByResponse



from .WarningsResponse import WarningsResponse



from .ModifiedByResponse import ModifiedByResponse





from .ContactNumberResponse import ContactNumberResponse











from .DocumentsResponse import DocumentsResponse



from .ProductReturnConfigResponse import ProductReturnConfigResponse



from .LogisticsResponse import LogisticsResponse



from .IntegrationTypeResponse import IntegrationTypeResponse









from .GstCredentialsResponse import GstCredentialsResponse





from .ManagerResponse import ManagerResponse



class ItemResponse(BaseSchema):
    #  swagger.json

    
    stage = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    code = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    

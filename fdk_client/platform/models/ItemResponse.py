"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CreatedByResponse import CreatedByResponse



from .DocumentsResponse import DocumentsResponse

from .IntegrationTypeResponse import IntegrationTypeResponse

from .ContactNumberResponse import ContactNumberResponse





from .ProductReturnConfigResponse import ProductReturnConfigResponse



from .LogisticsResponse import LogisticsResponse





from .ModifiedByResponse import ModifiedByResponse





from .GstCredentialsResponse import GstCredentialsResponse

from .ManagerResponse import ManagerResponse

from .WarningsResponse import WarningsResponse







from .TimmingResponse import TimmingResponse

from .AddressResponse import AddressResponse





from .ModifiedByResponse import ModifiedByResponse




class ItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    store_type = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    sub_type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    created_on = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    uid = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    code = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    _cls = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    company = fields.Int(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    stage = fields.Str(required=False)
    


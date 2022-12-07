"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ManagerResponse import ManagerResponse



from .TimmingResponse import TimmingResponse

from .ModifiedByResponse import ModifiedByResponse

from .WarningsResponse import WarningsResponse



from .AddressResponse import AddressResponse



from .DocumentsResponse import DocumentsResponse

from .ContactNumberResponse import ContactNumberResponse





from .GstCredentialsResponse import GstCredentialsResponse









from .ModifiedByResponse import ModifiedByResponse

from .CreatedByResponse import CreatedByResponse



from .IntegrationTypeResponse import IntegrationTypeResponse







from .ProductReturnConfigResponse import ProductReturnConfigResponse

from .LogisticsResponse import LogisticsResponse


class ItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    _cls = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    company_id = fields.Int(required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    sub_type = fields.Str(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company = fields.Int(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    


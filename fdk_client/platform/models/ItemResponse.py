"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CreatedByResponse import CreatedByResponse

from .GstCredentialsResponse import GstCredentialsResponse

from .TimmingResponse import TimmingResponse

from .LogisticsResponse import LogisticsResponse

from .ProductReturnConfigResponse import ProductReturnConfigResponse

from .DocumentsResponse import DocumentsResponse

from .ManagerResponse import ManagerResponse









from .ContactNumberResponse import ContactNumberResponse

from .AddressResponse import AddressResponse









from .ModifiedByResponse import ModifiedByResponse

from .IntegrationTypeResponse import IntegrationTypeResponse

from .WarningsResponse import WarningsResponse















from .ModifiedByResponse import ModifiedByResponse


class ItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    _cls = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    modified_on = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    


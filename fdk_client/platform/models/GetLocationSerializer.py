"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .GetCompanySerializer import GetCompanySerializer

from .UserSerializer2 import UserSerializer2

from .Document import Document







from .LocationIntegrationType import LocationIntegrationType

from .UserSerializer2 import UserSerializer2









from .GetAddressSerializer import GetAddressSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .SellerPhoneNumber import SellerPhoneNumber



from .LocationManagerSerializer import LocationManagerSerializer

from .UserSerializer2 import UserSerializer2


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer2, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    phone_number = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    created_by = fields.Nested(UserSerializer2, required=False)
    
    stage = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer2, required=False)
    


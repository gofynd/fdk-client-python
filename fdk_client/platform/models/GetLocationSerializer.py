"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .GetCompanySerializer import GetCompanySerializer

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .UserSerializer2 import UserSerializer2

from .UserSerializer2 import UserSerializer2



from .SellerPhoneNumber import SellerPhoneNumber



from .UserSerializer2 import UserSerializer2

from .LocationManagerSerializer import LocationManagerSerializer

from .Document import Document







from .LocationIntegrationType import LocationIntegrationType



from .GetAddressSerializer import GetAddressSerializer





from .LocationDayWiseSerializer import LocationDayWiseSerializer


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer2, required=False)
    
    verified_by = fields.Nested(UserSerializer2, required=False)
    
    display_name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer2, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    code = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    phone_number = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    


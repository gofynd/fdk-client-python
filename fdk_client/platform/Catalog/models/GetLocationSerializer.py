"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LocationManagerSerializer import LocationManagerSerializer





from .SellerPhoneNumber import SellerPhoneNumber

















from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .LocationIntegrationType import LocationIntegrationType







from .Document import Document





from .GetCompanySerializer import GetCompanySerializer



from .GetAddressSerializer import GetAddressSerializer





from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .UserSerializer2 import UserSerializer2



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .UserSerializer2 import UserSerializer2



from .UserSerializer2 import UserSerializer2



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    store_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer2, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer2, required=False)
    
    modified_by = fields.Nested(UserSerializer2, required=False)
    

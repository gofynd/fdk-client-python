"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LocationIntegrationType import LocationIntegrationType



from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .UserSerializer1 import UserSerializer1









from .ProductReturnConfigSerializer import ProductReturnConfigSerializer





from .GetAddressSerializer import GetAddressSerializer







from .UserSerializer1 import UserSerializer1









from .SellerPhoneNumber import SellerPhoneNumber





from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .Document import Document



from .GetCompanySerializer import GetCompanySerializer



from .UserSerializer1 import UserSerializer1







from .LocationManagerSerializer import LocationManagerSerializer



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    warnings = fields.Dict(required=False)
    
    store_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    phone_number = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
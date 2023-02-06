"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer













from .UserSerializer1 import UserSerializer1





from .Document import Document





from .LocationManagerSerializer import LocationManagerSerializer



from .UserSerializer1 import UserSerializer1













from .SellerPhoneNumber import SellerPhoneNumber



from .GetAddressSerializer import GetAddressSerializer



from .GetCompanySerializer import GetCompanySerializer





from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .LocationIntegrationType import LocationIntegrationType



from .UserSerializer1 import UserSerializer1



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    store_type = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    

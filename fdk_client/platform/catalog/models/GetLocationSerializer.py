"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSerializer1 import UserSerializer1





from .UserSerializer1 import UserSerializer1





from .LocationDayWiseSerializer import LocationDayWiseSerializer





from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .GetAddressSerializer import GetAddressSerializer



from .UserSerializer1 import UserSerializer1



from .GetCompanySerializer import GetCompanySerializer



from .LocationIntegrationType import LocationIntegrationType













from .SellerPhoneNumber import SellerPhoneNumber











from .LocationManagerSerializer import LocationManagerSerializer



from .Document import Document





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    uid = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    phone_number = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    

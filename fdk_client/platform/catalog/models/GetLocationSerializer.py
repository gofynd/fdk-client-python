"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSerializer1 import UserSerializer1



from .SellerPhoneNumber import SellerPhoneNumber



from .LocationIntegrationType import LocationIntegrationType







from .UserSerializer1 import UserSerializer1



from .UserSerializer1 import UserSerializer1





from .GetAddressSerializer import GetAddressSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer







from .Document import Document







from .LocationManagerSerializer import LocationManagerSerializer



from .GetCompanySerializer import GetCompanySerializer











from .LocationDayWiseSerializer import LocationDayWiseSerializer





class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    phone_number = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    stage = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    

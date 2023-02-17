"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSerializer1 import UserSerializer1











from .GetAddressSerializer import GetAddressSerializer





from .Document import Document





from .UserSerializer1 import UserSerializer1



from .SellerPhoneNumber import SellerPhoneNumber





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .LocationIntegrationType import LocationIntegrationType



from .LocationManagerSerializer import LocationManagerSerializer



from .UserSerializer1 import UserSerializer1





from .GetCompanySerializer import GetCompanySerializer







from .InvoiceDetailsSerializer import InvoiceDetailsSerializer







from .LocationDayWiseSerializer import LocationDayWiseSerializer





class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    code = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    store_type = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    

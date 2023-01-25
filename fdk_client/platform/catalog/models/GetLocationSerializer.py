"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .UserSerializer1 import UserSerializer1





from .SellerPhoneNumber import SellerPhoneNumber





from .Document import Document





from .LocationIntegrationType import LocationIntegrationType







from .GetCompanySerializer import GetCompanySerializer





from .LocationManagerSerializer import LocationManagerSerializer



from .UserSerializer1 import UserSerializer1





from .LocationDayWiseSerializer import LocationDayWiseSerializer





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer









from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .GetAddressSerializer import GetAddressSerializer



from .UserSerializer1 import UserSerializer1





class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    phone_number = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    code = fields.Str(required=False)
    

"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .LocationManagerSerializer import LocationManagerSerializer





from .Document import Document



from .GetAddressSerializer import GetAddressSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer













from .HolidaySchemaSerializer import HolidaySchemaSerializer





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .SellerPhoneNumber import SellerPhoneNumber







class LocationSerializer(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    company = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSerializer, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    code = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    

"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .HolidaySchemaSerializer import HolidaySchemaSerializer









from .SellerPhoneNumber import SellerPhoneNumber







from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .GetAddressSerializer import GetAddressSerializer





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .LocationManagerSerializer import LocationManagerSerializer







from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .Document import Document



class LocationSerializer(BaseSchema):
    #  swagger.json

    
    company = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSerializer, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    

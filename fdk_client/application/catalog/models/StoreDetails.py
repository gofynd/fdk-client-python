"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .StoreManagerSerializer import StoreManagerSerializer



from .CompanyStore import CompanyStore



from .StoreDepartments import StoreDepartments





from .StoreAddressSerializer import StoreAddressSerializer



from .StoreTiming import StoreTiming



from .SellerPhoneNumber import SellerPhoneNumber





class StoreDetails(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    

"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StoreManagerSerializer import StoreManagerSerializer



from .CompanyStore import CompanyStore



from .SellerPhoneNumber import SellerPhoneNumber



from .StoreAddressSerializer import StoreAddressSerializer



from .StoreDepartments import StoreDepartments





from .StoreTiming import StoreTiming







class StoreDetails(BaseSchema):
    #  swagger.json

    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    

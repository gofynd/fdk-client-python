"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StoreAddressSerializer import StoreAddressSerializer





from .CompanyStore import CompanyStore



from .StoreManagerSerializer import StoreManagerSerializer



from .SellerPhoneNumber import SellerPhoneNumber



from .StoreTiming import StoreTiming





from .StoreDepartments import StoreDepartments





class StoreDetails(BaseSchema):
    #  swagger.json

    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    uid = fields.Int(required=False)
    

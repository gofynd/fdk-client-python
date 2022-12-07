"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SellerPhoneNumber import SellerPhoneNumber



from .StoreDepartments import StoreDepartments







from .CompanyStore import CompanyStore



from .StoreAddressSerializer import StoreAddressSerializer



from .StoreTiming import StoreTiming





from .StoreManagerSerializer import StoreManagerSerializer



class StoreDetails(BaseSchema):
    #  swagger.json

    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

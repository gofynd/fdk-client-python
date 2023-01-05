"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StoreTiming import StoreTiming





from .StoreAddressSerializer import StoreAddressSerializer



from .SellerPhoneNumber import SellerPhoneNumber



from .CompanyStore import CompanyStore







from .StoreManagerSerializer import StoreManagerSerializer



from .StoreDepartments import StoreDepartments



class StoreDetails(BaseSchema):
    #  swagger.json

    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    

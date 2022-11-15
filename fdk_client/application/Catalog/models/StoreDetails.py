"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CompanyStore import CompanyStore



from .StoreTiming import StoreTiming



from .StoreDepartments import StoreDepartments



from .StoreAddressSerializer import StoreAddressSerializer







from .SellerPhoneNumber import SellerPhoneNumber



from .StoreManagerSerializer import StoreManagerSerializer



class StoreDetails(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

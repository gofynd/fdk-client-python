"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CompanyStore import CompanyStore





from .StoreDepartments import StoreDepartments



from .SellerPhoneNumber import SellerPhoneNumber



from .StoreAddressSerializer import StoreAddressSerializer



from .StoreManagerSerializer import StoreManagerSerializer



class AppStore(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
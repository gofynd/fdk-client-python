"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SellerPhoneNumber import SellerPhoneNumber



from .CompanyStore import CompanyStore



from .StoreManagerSerializer import StoreManagerSerializer







from .StoreDepartments import StoreDepartments



from .StoreAddressSerializer import StoreAddressSerializer



class AppStore(BaseSchema):
    #  swagger.json

    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    

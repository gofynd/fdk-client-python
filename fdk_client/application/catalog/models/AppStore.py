"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .StoreDepartments import StoreDepartments



from .CompanyStore import CompanyStore



from .StoreAddressSerializer import StoreAddressSerializer



from .SellerPhoneNumber import SellerPhoneNumber





from .StoreManagerSerializer import StoreManagerSerializer



class AppStore(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

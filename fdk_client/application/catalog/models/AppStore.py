"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StoreAddressSerializer import StoreAddressSerializer





from .CompanyStore import CompanyStore



from .SellerPhoneNumber import SellerPhoneNumber





from .StoreDepartments import StoreDepartments



from .StoreManagerSerializer import StoreManagerSerializer



class AppStore(BaseSchema):
    #  swagger.json

    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

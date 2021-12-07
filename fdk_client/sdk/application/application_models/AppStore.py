"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CompanyStore import CompanyStore

from .StoreDepartments import StoreDepartments

from .StoreAddressSerializer import StoreAddressSerializer

from .SellerPhoneNumber import SellerPhoneNumber



from .StoreManagerSerializer import StoreManagerSerializer




class AppStore(BaseSchema):

    
    company = fields.Nested(CompanyStore, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    name = fields.Str(required=False)
    


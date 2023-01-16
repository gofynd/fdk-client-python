"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .UserSerializer import UserSerializer





from .GetBrandResponseSerializer import GetBrandResponseSerializer



from .UserSerializer import UserSerializer





from .CompanySerializer import CompanySerializer







from .UserSerializer import UserSerializer





class CompanyBrandSerializer(BaseSchema):
    #  swagger.json

    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    

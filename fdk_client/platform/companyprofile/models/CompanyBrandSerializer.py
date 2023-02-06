"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CompanySerializer import CompanySerializer



from .UserSerializer import UserSerializer







from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer







from .GetBrandResponseSerializer import GetBrandResponseSerializer









class CompanyBrandSerializer(BaseSchema):
    #  swagger.json

    
    company = fields.Nested(CompanySerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    

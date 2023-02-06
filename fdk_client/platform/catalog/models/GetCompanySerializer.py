"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSerializer2 import UserSerializer2









from .UserSerializer2 import UserSerializer2



from .UserSerializer2 import UserSerializer2











from .GetAddressSerializer import GetAddressSerializer







class GetCompanySerializer(BaseSchema):
    #  swagger.json

    
    verified_by = fields.Nested(UserSerializer2, required=False)
    
    company_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer2, required=False)
    
    created_by = fields.Nested(UserSerializer2, required=False)
    
    verified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    business_type = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

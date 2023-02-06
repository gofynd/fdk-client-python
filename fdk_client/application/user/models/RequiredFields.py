"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PlatformEmail import PlatformEmail



from .PlatformMobile import PlatformMobile



class RequiredFields(BaseSchema):
    #  swagger.json

    
    email = fields.Nested(PlatformEmail, required=False)
    
    mobile = fields.Nested(PlatformMobile, required=False)
    

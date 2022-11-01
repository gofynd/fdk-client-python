"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PhoneSchema import PhoneSchema



from .EmailSchema import EmailSchema



class ContactSchema(BaseSchema):
    #  swagger.json

    
    phone = fields.Nested(PhoneSchema, required=False)
    
    email = fields.Nested(EmailSchema, required=False)
    

"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .RegisterRequiredFieldsEmail import RegisterRequiredFieldsEmail



from .RegisterRequiredFieldsMobile import RegisterRequiredFieldsMobile



class RegisterRequiredFields(BaseSchema):
    #  swagger.json

    
    email = fields.Nested(RegisterRequiredFieldsEmail, required=False)
    
    mobile = fields.Nested(RegisterRequiredFieldsMobile, required=False)
    

"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .RegisterRequiredFieldsEmail import RegisterRequiredFieldsEmail

from .RegisterRequiredFieldsMobile import RegisterRequiredFieldsMobile


class RegisterRequiredFields(BaseSchema):

    
    email = fields.Nested(RegisterRequiredFieldsEmail, required=False)
    
    mobile = fields.Nested(RegisterRequiredFieldsMobile, required=False)
    


"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .EmailProperties import EmailProperties


class EmailSchema(BaseSchema):
    # Content swagger.json

    
    active = fields.Boolean(required=False)
    
    email = fields.List(fields.Nested(EmailProperties, required=False), required=False)
    


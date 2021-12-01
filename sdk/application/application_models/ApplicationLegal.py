"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema









from .ApplicationLegalFAQ import ApplicationLegalFAQ








class ApplicationLegal(BaseSchema):

    
    application = fields.Str(required=False)
    
    tnc = fields.Str(required=False)
    
    policy = fields.Str(required=False)
    
    shipping = fields.Str(required=False)
    
    faq = fields.List(fields.Nested(ApplicationLegalFAQ, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


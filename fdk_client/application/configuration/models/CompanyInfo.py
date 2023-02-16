"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














from .CompanyAboutAddress import CompanyAboutAddress





class CompanyInfo(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(CompanyAboutAddress, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    

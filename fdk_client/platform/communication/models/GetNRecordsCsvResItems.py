"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class GetNRecordsCsvResItems(BaseSchema):
    #  swagger.json

    
    phone_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    firstname = fields.Str(required=False)
    
    lastname = fields.Str(required=False)
    
    orderid = fields.Str(required=False)
    

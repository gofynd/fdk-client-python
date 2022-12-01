"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CODdata import CODdata



class GetUserCODLimitResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    user_cod_data = fields.Nested(CODdata, required=False)
    

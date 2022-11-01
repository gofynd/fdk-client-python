"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TransferModeDetails import TransferModeDetails



class TransferModeResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(TransferModeDetails, required=False), required=False)
    

"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class IntentAppErrorList(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    package_name = fields.Str(required=False)
    

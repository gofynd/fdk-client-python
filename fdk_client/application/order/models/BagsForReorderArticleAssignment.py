"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class BagsForReorderArticleAssignment(BaseSchema):
    #  swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

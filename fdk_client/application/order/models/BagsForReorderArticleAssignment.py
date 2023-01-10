"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class BagsForReorderArticleAssignment(BaseSchema):
    #  swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    

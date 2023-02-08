"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class JioCodeUpsertDataSet(BaseSchema):
    #  swagger.json

    
    article_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    item_id = fields.Str(required=False)
    
    jio_code = fields.Str(required=False)
    

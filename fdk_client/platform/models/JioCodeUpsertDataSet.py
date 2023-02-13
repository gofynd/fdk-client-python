"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class JioCodeUpsertDataSet(BaseSchema):
    # Orders swagger.json

    
    article_id = fields.Str(required=False)
    
    item_id = fields.Str(required=False)
    
    jio_code = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    

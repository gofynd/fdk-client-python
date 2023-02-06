"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class BulkBundleRestriction(BaseSchema):
    #  swagger.json

    
    multi_store_allowed = fields.Boolean(required=False)
    

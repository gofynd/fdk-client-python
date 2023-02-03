"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .VerifiedBy import VerifiedBy







from .ProductDownloadItemsData import ProductDownloadItemsData













class ProductDownloadsItems(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    created_by = fields.Nested(VerifiedBy, required=False)
    
    id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    data = fields.Nested(ProductDownloadItemsData, required=False)
    
    completed_on = fields.Str(required=False)
    
    seller_id = fields.Float(required=False)
    
    template_tags = fields.Dict(required=False)
    
    trigger_on = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    

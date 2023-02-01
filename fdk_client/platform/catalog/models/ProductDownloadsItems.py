"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductDownloadItemsData import ProductDownloadItemsData



from .VerifiedBy import VerifiedBy



















class ProductDownloadsItems(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(ProductDownloadItemsData, required=False)
    
    created_by = fields.Nested(VerifiedBy, required=False)
    
    trigger_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Float(required=False)
    
    id = fields.Str(required=False)
    
    completed_on = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    template_tags = fields.Dict(required=False)
    

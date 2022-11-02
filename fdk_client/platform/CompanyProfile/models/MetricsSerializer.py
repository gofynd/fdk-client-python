"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DocumentsObj import DocumentsObj



from .DocumentsObj import DocumentsObj





from .DocumentsObj import DocumentsObj





from .DocumentsObj import DocumentsObj



from .DocumentsObj import DocumentsObj



class MetricsSerializer(BaseSchema):
    #  swagger.json

    
    store = fields.Nested(DocumentsObj, required=False)
    
    brand = fields.Nested(DocumentsObj, required=False)
    
    uid = fields.Int(required=False)
    
    store_documents = fields.Nested(DocumentsObj, required=False)
    
    stage = fields.Str(required=False)
    
    company_documents = fields.Nested(DocumentsObj, required=False)
    
    product = fields.Nested(DocumentsObj, required=False)
    
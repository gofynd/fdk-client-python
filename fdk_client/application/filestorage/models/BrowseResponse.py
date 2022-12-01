"""filestorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .DbRecord import DbRecord



from .Page import Page



class BrowseResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(DbRecord, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

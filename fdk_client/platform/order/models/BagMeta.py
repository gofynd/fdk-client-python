"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .B2BPODetails import B2BPODetails



class BagMeta(BaseSchema):
    #  swagger.json

    
    b2b_po_details = fields.Nested(B2BPODetails, required=False)
    

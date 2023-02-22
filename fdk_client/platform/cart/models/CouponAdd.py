"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Rule import Rule



from .Restrictions import Restrictions



from .RuleDefinition import RuleDefinition



from .CouponAction import CouponAction



from .CouponSchedule import CouponSchedule



from .DisplayMeta import DisplayMeta



from .Identifier import Identifier



from .Ownership import Ownership



from .Validity import Validity



from .CouponAuthor import CouponAuthor







from .Validation import Validation



from .CouponDateMeta import CouponDateMeta



from .State import State





class CouponAdd(BaseSchema):
    #  swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

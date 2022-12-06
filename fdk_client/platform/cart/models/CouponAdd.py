"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponSchedule import CouponSchedule





from .Restrictions import Restrictions



from .Ownership import Ownership



from .CouponAction import CouponAction



from .Rule import Rule



from .Identifier import Identifier



from .CouponAuthor import CouponAuthor



from .CouponDateMeta import CouponDateMeta



from .RuleDefinition import RuleDefinition



from .Validity import Validity





from .Validation import Validation





from .DisplayMeta import DisplayMeta



from .State import State



class CouponAdd(BaseSchema):
    #  swagger.json

    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    state = fields.Nested(State, required=False)
    

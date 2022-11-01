"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Rule import Rule



from .Validation import Validation





from .CouponAction import CouponAction



from .State import State



from .RuleDefinition import RuleDefinition





from .DisplayMeta import DisplayMeta



from .Ownership import Ownership



from .CouponAuthor import CouponAuthor



from .Identifier import Identifier



from .CouponDateMeta import CouponDateMeta



from .Validity import Validity



from .CouponSchedule import CouponSchedule



from .Restrictions import Restrictions





class CouponAdd(BaseSchema):
    #  swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    

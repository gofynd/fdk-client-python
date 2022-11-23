"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .State import State



from .CouponAction import CouponAction





from .Rule import Rule





from .Identifier import Identifier



from .Restrictions import Restrictions



from .Validation import Validation



from .RuleDefinition import RuleDefinition



from .Validity import Validity



from .CouponAuthor import CouponAuthor



from .DisplayMeta import DisplayMeta



from .CouponDateMeta import CouponDateMeta





from .Ownership import Ownership



from .CouponSchedule import CouponSchedule



class CouponAdd(BaseSchema):
    #  swagger.json

    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    

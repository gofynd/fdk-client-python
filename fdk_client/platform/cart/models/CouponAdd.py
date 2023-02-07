"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Validation import Validation



from .RuleDefinition import RuleDefinition





from .Identifier import Identifier



from .Ownership import Ownership



from .CouponAuthor import CouponAuthor



from .CouponAction import CouponAction



from .DisplayMeta import DisplayMeta



from .CouponSchedule import CouponSchedule



from .Validity import Validity



from .Rule import Rule





from .State import State



from .CouponDateMeta import CouponDateMeta



from .Restrictions import Restrictions



class CouponAdd(BaseSchema):
    #  swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    

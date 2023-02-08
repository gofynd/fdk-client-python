"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Validity import Validity





from .Validation import Validation



from .Identifier import Identifier



from .Restrictions import Restrictions



from .RuleDefinition import RuleDefinition





from .DisplayMeta import DisplayMeta



from .CouponDateMeta import CouponDateMeta



from .Rule import Rule





from .CouponSchedule import CouponSchedule



from .CouponAction import CouponAction



from .State import State



from .CouponAuthor import CouponAuthor



from .Ownership import Ownership



class CouponAdd(BaseSchema):
    #  swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    

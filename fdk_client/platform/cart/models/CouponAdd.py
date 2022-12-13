"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .RuleDefinition import RuleDefinition



from .CouponDateMeta import CouponDateMeta



from .State import State



from .DisplayMeta import DisplayMeta



from .Validity import Validity



from .Validation import Validation



from .Identifier import Identifier



from .Ownership import Ownership



from .CouponSchedule import CouponSchedule





from .CouponAuthor import CouponAuthor





from .CouponAction import CouponAction



from .Restrictions import Restrictions



from .Rule import Rule





class CouponAdd(BaseSchema):
    #  swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    state = fields.Nested(State, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    

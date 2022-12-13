"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .RuleDefinition import RuleDefinition



from .CouponSchedule import CouponSchedule



from .State import State



from .CouponAction import CouponAction



from .Identifier import Identifier



from .CouponDateMeta import CouponDateMeta



from .Ownership import Ownership





from .Validation import Validation



from .Validity import Validity





from .Restrictions import Restrictions



from .CouponAuthor import CouponAuthor





from .DisplayMeta import DisplayMeta



from .Rule import Rule



class CouponAdd(BaseSchema):
    #  swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    

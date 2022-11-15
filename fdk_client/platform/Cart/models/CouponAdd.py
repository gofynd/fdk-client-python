"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponAction import CouponAction



from .Identifier import Identifier



from .Restrictions import Restrictions



from .CouponSchedule import CouponSchedule



from .Ownership import Ownership



from .RuleDefinition import RuleDefinition



from .State import State



from .Validation import Validation



from .CouponAuthor import CouponAuthor







from .CouponDateMeta import CouponDateMeta



from .Rule import Rule



from .Validity import Validity





from .DisplayMeta import DisplayMeta



class CouponAdd(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    

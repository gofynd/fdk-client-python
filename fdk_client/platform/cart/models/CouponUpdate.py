"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DisplayMeta import DisplayMeta



from .CouponDateMeta import CouponDateMeta



from .CouponAuthor import CouponAuthor



from .CouponSchedule import CouponSchedule



from .RuleDefinition import RuleDefinition



from .Ownership import Ownership



from .Rule import Rule



from .Validity import Validity



from .Validation import Validation





from .Restrictions import Restrictions







from .State import State



from .Identifier import Identifier



from .CouponAction import CouponAction



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    

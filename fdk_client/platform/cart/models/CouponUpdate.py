"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponDateMeta import CouponDateMeta



from .Validity import Validity



from .RuleDefinition import RuleDefinition



from .CouponSchedule import CouponSchedule



from .Restrictions import Restrictions



from .Identifier import Identifier



from .CouponAuthor import CouponAuthor



from .State import State



from .Rule import Rule



from .CouponAction import CouponAction



from .Ownership import Ownership



from .Validation import Validation







from .DisplayMeta import DisplayMeta





class CouponUpdate(BaseSchema):
    #  swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    

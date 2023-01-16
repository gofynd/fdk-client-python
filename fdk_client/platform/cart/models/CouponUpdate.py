"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Identifier import Identifier



from .CouponAuthor import CouponAuthor





from .Restrictions import Restrictions



from .State import State



from .CouponSchedule import CouponSchedule



from .Validity import Validity





from .Ownership import Ownership



from .Validation import Validation



from .CouponDateMeta import CouponDateMeta



from .RuleDefinition import RuleDefinition



from .CouponAction import CouponAction



from .Rule import Rule



from .DisplayMeta import DisplayMeta





class CouponUpdate(BaseSchema):
    #  swagger.json

    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    state = fields.Nested(State, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    type_slug = fields.Str(required=False)
    

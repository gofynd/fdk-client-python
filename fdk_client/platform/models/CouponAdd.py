"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Rule import Rule

from .State import State



from .CouponAction import CouponAction



from .Validation import Validation

from .DisplayMeta import DisplayMeta

from .CouponSchedule import CouponSchedule

from .Restrictions import Restrictions

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .CouponAuthor import CouponAuthor

from .RuleDefinition import RuleDefinition

from .Ownership import Ownership

from .Validity import Validity


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validity = fields.Nested(Validity, required=False)
    


"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .RuleDefinition import RuleDefinition

from .Validation import Validation



from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .Validity import Validity



from .Ownership import Ownership

from .CouponSchedule import CouponSchedule

from .State import State

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .CouponAction import CouponAction

from .Rule import Rule

from .Identifier import Identifier


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    type_slug = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    


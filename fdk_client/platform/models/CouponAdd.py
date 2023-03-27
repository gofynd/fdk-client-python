"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State

from .Rule import Rule

from .Identifier import Identifier



from .CouponDateMeta import CouponDateMeta

from .CouponAction import CouponAction

from .Validity import Validity



from .CouponSchedule import CouponSchedule

from .Validation import Validation

from .CouponAuthor import CouponAuthor



from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .Ownership import Ownership

from .RuleDefinition import RuleDefinition


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    code = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    


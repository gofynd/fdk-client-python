"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validity import Validity

from .State import State

from .CouponDateMeta import CouponDateMeta

from .Restrictions import Restrictions

from .CouponAction import CouponAction

from .CouponSchedule import CouponSchedule



from .Rule import Rule

from .Identifier import Identifier





from .CouponAuthor import CouponAuthor

from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    state = fields.Nested(State, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    


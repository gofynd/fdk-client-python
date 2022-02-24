"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .CouponAction import CouponAction

from .Identifier import Identifier

from .Validation import Validation

from .Ownership import Ownership





from .Rule import Rule

from .CouponAuthor import CouponAuthor

from .State import State

from .CouponSchedule import CouponSchedule



from .DisplayMeta import DisplayMeta

from .Validity import Validity

from .Restrictions import Restrictions


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    


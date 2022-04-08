"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Identifier import Identifier



from .Validity import Validity

from .Restrictions import Restrictions



from .CouponSchedule import CouponSchedule



from .RuleDefinition import RuleDefinition

from .Rule import Rule

from .CouponDateMeta import CouponDateMeta

from .DisplayMeta import DisplayMeta

from .CouponAuthor import CouponAuthor

from .State import State

from .CouponAction import CouponAction

from .Validation import Validation

from .Ownership import Ownership


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    


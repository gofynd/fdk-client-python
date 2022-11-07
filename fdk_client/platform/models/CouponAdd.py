"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .Validity import Validity

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership

from .CouponDateMeta import CouponDateMeta



from .CouponAuthor import CouponAuthor

from .CouponAction import CouponAction



from .Rule import Rule



from .State import State

from .Restrictions import Restrictions

from .CouponSchedule import CouponSchedule

from .Identifier import Identifier


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    


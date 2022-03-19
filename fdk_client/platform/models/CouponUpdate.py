"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State



from .RuleDefinition import RuleDefinition

from .Restrictions import Restrictions

from .Validity import Validity

from .Ownership import Ownership





from .CouponDateMeta import CouponDateMeta

from .Validation import Validation

from .CouponAuthor import CouponAuthor

from .CouponAction import CouponAction

from .Rule import Rule

from .CouponSchedule import CouponSchedule

from .DisplayMeta import DisplayMeta

from .Identifier import Identifier


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    code = fields.Str(required=False)
    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    


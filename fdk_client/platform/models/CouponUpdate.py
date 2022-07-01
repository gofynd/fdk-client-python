"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta import DisplayMeta

from .CouponAuthor import CouponAuthor



from .Ownership import Ownership

from .Validation import Validation

from .CouponSchedule import CouponSchedule



from .Validity import Validity

from .Restrictions import Restrictions

from .CouponAction import CouponAction

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier



from .State import State

from .Rule import Rule

from .RuleDefinition import RuleDefinition


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    


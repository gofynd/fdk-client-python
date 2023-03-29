"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta import DisplayMeta



from .Ownership import Ownership

from .CouponDateMeta import CouponDateMeta

from .Validation import Validation

from .RuleDefinition import RuleDefinition





from .CouponSchedule import CouponSchedule

from .Restrictions import Restrictions

from .Validity import Validity

from .Identifier import Identifier

from .CouponAuthor import CouponAuthor

from .Rule import Rule

from .State import State

from .CouponAction import CouponAction


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    


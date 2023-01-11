"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponAuthor import CouponAuthor

from .Identifier import Identifier

from .CouponDateMeta import CouponDateMeta

from .Ownership import Ownership

from .Rule import Rule

from .CouponSchedule import CouponSchedule





from .Validity import Validity

from .State import State

from .RuleDefinition import RuleDefinition



from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .Validation import Validation

from .CouponAction import CouponAction


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    


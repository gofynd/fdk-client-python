"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Rule import Rule

from .Validity import Validity



from .CouponAuthor import CouponAuthor

from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .CouponSchedule import CouponSchedule

from .DisplayMeta import DisplayMeta



from .CouponAction import CouponAction

from .Ownership import Ownership

from .State import State



from .Validation import Validation

from .Restrictions import Restrictions


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    state = fields.Nested(State, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    


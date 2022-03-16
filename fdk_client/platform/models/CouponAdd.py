"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponAction import CouponAction

from .CouponDateMeta import CouponDateMeta

from .RuleDefinition import RuleDefinition



from .Restrictions import Restrictions

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .Validation import Validation

from .DisplayMeta import DisplayMeta





from .Rule import Rule

from .CouponSchedule import CouponSchedule

from .State import State

from .Identifier import Identifier

from .Ownership import Ownership


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    action = fields.Nested(CouponAction, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    


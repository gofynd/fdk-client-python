"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validity import Validity

from .Validation import Validation

from .Rule import Rule

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership

from .State import State

from .CouponSchedule import CouponSchedule

from .CouponAction import CouponAction



from .CouponAuthor import CouponAuthor

from .RuleDefinition import RuleDefinition



from .Identifier import Identifier

from .CouponDateMeta import CouponDateMeta



from .Restrictions import Restrictions


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    state = fields.Nested(State, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    type_slug = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    


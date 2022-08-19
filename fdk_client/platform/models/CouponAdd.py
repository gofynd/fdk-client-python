"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State



from .Restrictions import Restrictions

from .Rule import Rule



from .Validation import Validation

from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule

from .Identifier import Identifier



from .CouponAction import CouponAction

from .Ownership import Ownership

from .DisplayMeta import DisplayMeta

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .RuleDefinition import RuleDefinition


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    


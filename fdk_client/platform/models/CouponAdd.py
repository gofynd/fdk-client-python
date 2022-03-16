"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta import DisplayMeta

from .Rule import Rule



from .RuleDefinition import RuleDefinition

from .State import State

from .Validity import Validity

from .CouponAction import CouponAction

from .CouponAuthor import CouponAuthor

from .Identifier import Identifier



from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule

from .Validation import Validation



from .Restrictions import Restrictions

from .Ownership import Ownership


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    


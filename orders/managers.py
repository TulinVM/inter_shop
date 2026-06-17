from django.db import models
from django.db.models import Sum, F, DecimalField


class OrderQuerySet(models.QuerySet):

    def new(self):
        return self.filter(status='new')

    def confirmed(self):
        return self.filter(status='confirmed')

    def shipped(self):
        return self.filter(status='shipped')

    def for_user(self, user):
        return self.filter(user=user)

    def total_sum(self):
        return self.annotate(
            total=Sum(
                F('items__price') * F('items__quantity'),
                output_field=DecimalField()
            )
        )

    def with_items(self):
        return self.prefetch_related(
            'items',
            'items__product'
        )
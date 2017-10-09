import datetime

from haystack import indexes
 
from .models import Ticket
 
 
class TicketIndex(indexes.SearchIndex, indexes.Indexable):
    # text = indexes.CharField(document=True, use_template=True)
    text = indexes.EdgeNgramField(indexed=True, document=True, use_template=True)
    name = indexes.CharField(stored=True, indexed=False, model_attr='name')
    detail = indexes.CharField(stored=True, indexed=False, model_attr='detail')
    price = indexes.CharField(stored=True, indexed=False, model_attr='price')
    expire_date = indexes.DateField(stored=True, indexed=False, model_attr='expire_date')
    currency = indexes.CharField(stored=True, indexed=False, model_attr='currency')
    ticket_image_url = indexes.CharField(stored=True, indexed=False, model_attr='ticket_image_url')
    available = indexes.BooleanField(stored=True, indexed=False, model_attr='available')
    # name = indexes.EdgeNgramField(model_attr='name')
    # detail = indexes.EdgeNgramField(model_attr='detail')
 
    def get_model(self):
        return Ticket
 
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(available=True)
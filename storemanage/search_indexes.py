import datetime

from haystack import indexes
 
from .models import Ticket
 
 
class TicketIndex(indexes.SearchIndex, indexes.Indexable):
    # text = indexes.CharField(document=True, use_template=True)
    text = indexes.EdgeNgramField(indexed=True, document=True, use_template=True)
    name = indexes.CharField(stored=True, indexed=False, model_attr='name')
    detail = indexes.CharField(stored=True, indexed=False, model_attr='detail')
    # name = indexes.EdgeNgramField(model_attr='name')
    # detail = indexes.EdgeNgramField(model_attr='detail')
 
    def get_model(self):
        return Ticket
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
from haystack import indexes
 
from storemanage.models import Ticket
 
 
class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
 
    def get_model(self):
        return Ticket
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
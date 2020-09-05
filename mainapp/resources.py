from import_export import resources
from .models import Article, ChoiceProgram


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article, ChoiceProgram

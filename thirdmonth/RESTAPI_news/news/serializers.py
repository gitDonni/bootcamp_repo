from rest_framework import serializers
from .models import News


# class NewsModel:
#     def __init__(self, author, title, description, category, created_at, published_date):
#         self.author = author
#         self.title = title
#         self.description = description
#         self.category = category
#         self.created_at = created_at
#         self.published_date = published_date


class NewsSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = '__all__'




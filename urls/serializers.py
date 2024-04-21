from rest_framework.response import Response
from rest_framework import serializers, status, viewsets, request
from .parser import Parser
from urls.models import Collection, Url


class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Collection
        fields = "__all__"


class CollectionForeignKeyByUser(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = Collection.objects.all()
        return queryset.filter(user=self.context['request'].user)


class UrlSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    collection = CollectionForeignKeyByUser(many=True, read_only=False)
    class Meta:
        model = Url
        fields = "__all__"

    def create(self, validated_data):
        try:
            parser = Parser(validated_data['url'])
            parsed_og_tags = parser.parse_page()
            for key, value in parsed_og_tags.items():
                if not validated_data[key[3:]]:
                    validated_data[key[3:]] = value
        finally:
            return super(UrlSerializer, self).create(validated_data)


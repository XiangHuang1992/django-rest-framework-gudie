from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     # 定义了序列化和反序列化的字段
#     # 此处我们发现SnippetSerializer和Snippet有太多重复的代码。类似于Django中的Form和ModelForm，REST framework
#     # 提供了Serializer和ModelSerializer。
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         如果数据合法就创建并返回一个snippets
#         :param validated_data:
#         :return:
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         如果数据合法就更新并返回一个存在snippet实例
#         :param instance:
#         :param validated_data:
#         :return:
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

# ModelSerializer 并没有使用任何黑科技，它仅仅是一个创建Serializer类的简单方法。
# 1.自动检测字段
# 2.简单的定义了create和update方法
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

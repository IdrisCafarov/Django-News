from dataclasses import fields
from modeltranslation.translator import translator,TranslationOptions
from blog.models import *

class CategoryOptions(TranslationOptions):
    fields = ('title',)
    

translator.register(Category,CategoryOptions)


class NewsOptions(TranslationOptions):
    fields = ('title','content',)

translator.register(News,NewsOptions)
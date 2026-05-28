import os
import django
import sys

# Устанавливаем кодировку UTF-8
sys.stdout.reconfigure(encoding='utf-8')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_prjct.settings')
django.setup()

from news_app.models import News
from slugify import slugify

print("Пересоздание slug'ов для новостей...")
count = 0

for news in News.objects.all():
    old_slug = news.slug
    news.slug = slugify(news.title)
    news.save()
    print(f"[OK] {news.title}")
    print(f"     {old_slug} -> {news.slug}")
    count += 1

print(f"\n[OK] Обновлено {count} новостей")

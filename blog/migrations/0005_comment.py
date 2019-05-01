# Generated by Django 2.1.3 on 2019-05-01 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190501_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(max_length=1000)),
                ('posted', models.DateField(auto_now_add=True, null=True, verbose_name='Post date')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='blog.Blog')),
            ],
        ),
    ]
# Generated by Django 2.0 on 2018-09-26 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-createtime'], 'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
        migrations.AlterModelOptions(
            name='blogtype',
            options={'verbose_name': '博客类型', 'verbose_name_plural': '博客类型'},
        ),
    ]
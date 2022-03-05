# Generated by Django 4.0.2 on 2022-02-20 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.base')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            bases=('blog.base',),
        ),
        migrations.AddField(
            model_name='post',
            name='base_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.base'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_name',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='category_name', to='blog.category'),
            preserve_default=False,
        ),
    ]
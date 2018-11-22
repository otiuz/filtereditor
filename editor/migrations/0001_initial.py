# Generated by Django 2.1.1 on 2018-11-22 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=100)),
                ('showhide', models.CharField(max_length=100)),
                ('rarity', models.CharField(max_length=100)),
                ('sound', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('beam', models.CharField(max_length=100)),
                ('section', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='editor.ItemSection')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSubSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsection', models.CharField(max_length=100)),
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='editor.ItemSection')),
            ],
        ),
        migrations.AddField(
            model_name='itemsettings',
            name='subsection',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='editor.ItemSubSection'),
        ),
    ]

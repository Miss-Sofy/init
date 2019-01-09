# Generated by Django 2.1 on 2018-10-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=64)),
                ('duration', models.DateTimeField()),
                ('multiple_choices', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Social_Media_accounts_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='success_storie',
            name='body',
            field=models.TextField(),
        ),
        migrations.RemoveField(
            model_name='user',
            name='Hobbies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Social_Media_accounts_names',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Sports',
        ),
        migrations.AddField(
            model_name='user',
            name='Hobbies',
            field=models.ManyToManyField(to='api.Hobby'),
        ),
        migrations.AddField(
            model_name='user',
            name='Social_Media_accounts_names',
            field=models.ManyToManyField(to='api.Social_Media_accounts_name'),
        ),
        migrations.AddField(
            model_name='user',
            name='Sports',
            field=models.ManyToManyField(to='api.Sport'),
        ),
    ]

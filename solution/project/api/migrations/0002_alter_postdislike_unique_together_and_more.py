# Generated by Django 4.2.10 on 2024-03-02 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postdislike',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='postdislike',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postdislike',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostDislike',
        ),
        migrations.DeleteModel(
            name='PostLike',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
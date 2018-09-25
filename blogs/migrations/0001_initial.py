# Generated by Django 2.1.1 on 2018-09-25 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shared.Content')),
            ],
            bases=('shared.content',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shared.Content')),
                ('title', models.CharField(max_length=150)),
                ('is_pinned', models.BooleanField(default=False)),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pin_board', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shared.PinBoard')),
            ],
            bases=('shared.content',),
        ),
        migrations.CreateModel(
            name='QnaAnswer',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shared.Content')),
                ('is_correct', models.BooleanField(default=False)),
            ],
            bases=('shared.content',),
        ),
        migrations.CreateModel(
            name='QnaQuestion',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shared.Content')),
                ('title', models.CharField(max_length=150)),
                ('is_live_question', models.BooleanField(default=False)),
            ],
            bases=('shared.content',),
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='qnaanswer',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.QnaQuestion'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Post'),
        ),
        migrations.AlterUniqueTogether(
            name='userfavorite',
            unique_together={('post', 'user')},
        ),
    ]

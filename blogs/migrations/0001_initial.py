# Generated by Django 2.1.1 on 2018-10-22 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livesession', '0001_initial'),
        ('shared', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('kind', models.CharField(default='Post', max_length=20)),
                ('is_pinned', models.BooleanField(default=False)),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pin_board', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shared.PinBoard')),
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
                ('kind', models.CharField(default='Question', max_length=20)),
                ('is_pinned', models.BooleanField(default=False)),
                ('is_live_question', models.BooleanField(default=False)),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='livesession.LiveQuestionSession')),
                ('pin_board', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shared.PinBoard')),
            ],
            bases=('shared.content',),
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
    ]

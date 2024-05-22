# Generated by Django 4.1.13 on 2024-05-22 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proiect', '0013_alter_uploadeddocument_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whats_wrong', models.TextField()),
                ('what_can_be_improved', models.TextField()),
                ('score', models.IntegerField()),
                ('decision', models.CharField(choices=[('reject', 'Reject'), ('accept_with_small_revisions', 'Accept with Small Revisions'), ('accept_with_major_revisions', 'Accept with Major Revisions'), ('accept', 'Accept')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proiect.uploadeddocument')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='uploadeddocument',
            name='feedback',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedback_documents', to='proiect.reviewfeedback'),
        ),
    ]

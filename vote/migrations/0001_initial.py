# Generated by Django 4.0.5 on 2022-07-03 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Party', models.CharField(blank=True, max_length=100, null=True)),
                ('Website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('StartDate', models.DateTimeField()),
                ('EndDate', models.DateTimeField()),
                ('IsActive', models.BooleanField(default=True)),
                ('ContractAddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.candidate')),
                ('Election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.election')),
                ('Voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='Election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.election'),
        ),
    ]

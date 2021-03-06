# Generated by Django 3.0.3 on 2020-03-10 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields
import scheduling_app.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('section', models.IntegerField()),
                ('school', django_enumfield.db.fields.EnumField(enum=scheduling_app.models.School)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('professor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('professor_type', django_enumfield.db.fields.EnumField(enum=scheduling_app.models.ProfessorType)),
                ('school', django_enumfield.db.fields.EnumField(enum=scheduling_app.models.School)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room_number', models.IntegerField()),
                ('building', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling_app.Course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling_app.Professor')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling_app.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Constraint',
            fields=[
                ('constraint_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_unavailable', models.TimeField()),
                ('can_be_broken', models.BooleanField(default=True)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling_app.Professor')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_workout_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='barbellrow',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='barbellrow2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='benchpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='benchpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='cablepulldown',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='cablepulldown2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='cablepushdown',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='cablepushdown2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='chestpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='chestpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='deadlift',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='deadlift2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dips',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dips2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dumbellbenchpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dumbellbenchpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dumbellrow',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dumbellrow2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dumbellshoulderpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='dumbellshoulderpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='frontraise',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='frontraise2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='inclinebenchpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='inclinebenchpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='innerthigh',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='innerthigh2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='lateralpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='lateralpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='legcurl',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='legcurl2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='legextension',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='legextension2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='legpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='legpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='letpulldown',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='letpulldown2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='lunge',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='lunge2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='militarypress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='militarypress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='overheadpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='overheadpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='pullup',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='pullup2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='seatedrow',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='seatedrow2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='shoulderpress',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='shoulderpress2',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='squat',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='squat2',
        ),
        migrations.AddField(
            model_name='workout',
            name='workoutlist',
            field=models.CharField(choices=[('deadlift', 'deadlift'), ('barbellrow', 'barbellrow'), ('dumbellrow', 'dumbellrow'), ('seatedrow', 'seatedrow'), ('pullup', 'pullup')], max_length=200, null=True),
        ),
    ]
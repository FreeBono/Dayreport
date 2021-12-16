# Generated by Django 3.2.9 on 2021-12-10 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20211210_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='barbellrow',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='benchpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='cablepulldown',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='cablepushdown',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='chestpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='deadlift',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='dips',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='dumbellbenchpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='dumbellrow',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='dumbellshoulderpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='frontraise',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='inclinebenchpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='innerthigh',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='lateralpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='legcurl',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='legextension',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='legpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='letpulldown',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='lunge',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='militarypress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='overheadpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='pullup',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='seatedrow',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='shoulderpress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='squat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='workoutinfo',
            name='workout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workoutinfo', to='contents.workout'),
        ),
    ]

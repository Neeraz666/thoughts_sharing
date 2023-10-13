
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.IntegerField(primary_key=True, serialize=False)),
            ]
        )
    ]
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("UserId", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
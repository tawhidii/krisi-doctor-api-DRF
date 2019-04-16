# Generated by Django 2.1.7 on 2019-03-26 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('krisi_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='problem_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('phone', models.CharField(max_length=50)),
                ('krisi_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krisi_user.krisi_user')),
            ],
        ),
    ]
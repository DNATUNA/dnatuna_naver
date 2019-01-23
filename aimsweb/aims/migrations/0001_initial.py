# Generated by Django 2.0.5 on 2018-11-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rheed_id', models.CharField(max_length=100)),
                ('run_id', models.CharField(max_length=100)),
                ('layer_id', models.CharField(max_length=100)),
                ('layer_name', models.CharField(max_length=100)),
                ('engineer_name', models.CharField(max_length=100)),
                ('rheed_start_date', models.DateTimeField(blank=True, null=True)),
                ('video_time', models.CharField(blank=True, max_length=100, null=True)),
                ('frame_num', models.CharField(blank=True, max_length=100, null=True)),
                ('rheed_video_filename', models.CharField(max_length=100)),
                ('rheed_video_input', models.CharField(max_length=100)),
                ('rheed_video_output', models.CharField(max_length=100)),
                ('chart1_json_json_filename', models.CharField(blank=True, max_length=100, null=True)),
                ('chart2_json_json_filename', models.CharField(blank=True, max_length=100, null=True)),
                ('chart3_json_json_filename', models.CharField(blank=True, max_length=100, null=True)),
                ('real_qual', models.CharField(blank=True, max_length=100, null=True)),
                ('equiv_id', models.CharField(blank=True, max_length=100, null=True)),
                ('product_type', models.CharField(blank=True, max_length=100, null=True)),
                ('setting_id', models.CharField(blank=True, max_length=100, null=True)),
                ('env_info', models.CharField(blank=True, max_length=100, null=True)),
                ('recipes_id', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('use_yn', models.TextField(blank=True, default='Y', max_length=1)),
                ('prediction_qual', models.CharField(blank=True, max_length=100, null=True)),
                ('prediction_model', models.CharField(blank=True, max_length=100, null=True)),
                ('pred_version', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
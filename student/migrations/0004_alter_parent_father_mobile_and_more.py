# Generated by Django 5.1.1 on 2024-09-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0003_parent_mother_occupation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parent",
            name="father_mobile",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="parent",
            name="father_occupation",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="parent",
            name="mother_mobile",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="parent",
            name="mother_occupation",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="student",
            name="admission_number",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female"), ("Others", "Others")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="religion",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="student",
            name="section",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_class",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_image",
            field=models.ImageField(blank=True, upload_to="students/"),
        ),
    ]

# Generated by Django 4.2.7 on 2024-10-24 12:44

import Mapapi.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(db_index=True, max_length=255)),
                ('question', models.TextField(db_index=True)),
                ('answer', models.TextField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True)),
                ('motivation', models.TextField(blank=True, null=True)),
                ('other_option', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Communaute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objet', models.CharField(max_length=250)),
                ('message', models.TextField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('zone', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(null=True)),
                ('lieu', models.CharField(max_length=250)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('audio', models.FileField(blank=True, null=True, upload_to='')),
                ('latitude', models.CharField(blank=True, max_length=1000, null=True)),
                ('longitude', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('zone', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('video', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('lattitude', models.CharField(blank=True, max_length=250, null=True)),
                ('longitude', models.CharField(blank=True, max_length=250, null=True)),
                ('etat', models.CharField(choices=[('declared', 'declared'), ('resolved', 'resolved'), ('in_progress', 'in_progress'), ('taken_into_account', 'taken_into_account')], default='declared', max_length=255)),
                ('slug', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category_id', models.ForeignKey(db_column='categ_incid_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_category', to='Mapapi.category')),
                ('category_ids', models.ManyToManyField(blank=True, to='Mapapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Indicateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objet', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('communaute', models.ForeignKey(db_column='mess_communaute_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communaute_mess', to='Mapapi.communaute')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('otp_code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_id', models.CharField(max_length=255)),
                ('incident_id', models.CharField(max_length=255)),
                ('incident_type', models.CharField(max_length=255)),
                ('piste_solution', models.TextField()),
                ('analysis', models.TextField()),
                ('ndvi_heatmap', models.TextField(blank=True, null=True)),
                ('ndvi_ndwi_plot', models.TextField(blank=True, null=True)),
                ('landcover_plot', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('lattitude', models.CharField(blank=True, max_length=250, null=True)),
                ('longitude', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='phone number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, default='avatars/default.png', null=True, upload_to='avatars/')),
                ('password_reset_count', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='adress')),
                ('user_type', models.CharField(choices=[('admin', 'admin'), ('visitor', 'visitor'), ('reporter', 'reporter'), ('citizen', 'citizen'), ('business', 'business'), ('elu', 'elu')], default='citizen', max_length=15)),
                ('provider', models.CharField(blank=True, max_length=255, null=True, verbose_name='provider')),
                ('organisation', models.CharField(blank=True, max_length=255, null=True)),
                ('points', models.IntegerField(blank=True, default=0, null=True)),
                ('community', models.ForeignKey(blank=True, db_column='user_communaute_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_communaute', to='Mapapi.communaute')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='mapapi_user_user_permissions', to='auth.permission', verbose_name='user permissions')),
                ('zones', models.ManyToManyField(blank=True, to='Mapapi.zone')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', Mapapi.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('timeStamp', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('elu', models.ForeignKey(db_column='user_mess_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_resp', to=settings.AUTH_USER_MODEL)),
                ('message', models.ForeignKey(db_column='mess_resp_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resp_mess', to='Mapapi.message')),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=500)),
                ('type', models.CharField(blank=True, max_length=500, null=True)),
                ('zone', models.CharField(max_length=250, null=True)),
                ('date_livraison', models.CharField(blank=True, max_length=100, null=True)),
                ('statut', models.CharField(choices=[('new', 'new'), ('in_progress', 'in_progress'), ('edit', 'edit'), ('canceled', 'canceled')], default='new', max_length=15)),
                ('disponible', models.BooleanField(default=False, verbose_name='active')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('incident', models.ForeignKey(db_column='incident_rapport_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incident_rapport', to='Mapapi.incident')),
                ('incidents', models.ManyToManyField(blank=True, to='Mapapi.incident')),
                ('user_id', models.ForeignKey(db_column='user_rapport_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rapport', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('used', models.BooleanField(default=False)),
                ('date_used', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('evenement_id', models.ForeignKey(db_column='event_participate_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_participate', to='Mapapi.evenement')),
                ('user_id', models.ForeignKey(db_column='user_participate_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_participate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('colaboration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mapapi.collaboration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(db_column='user_mess_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_mess', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='zone',
            field=models.ForeignKey(db_column='mess_zone_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zone_mess', to='Mapapi.zone'),
        ),
        migrations.AddField(
            model_name='incident',
            name='indicateur_id',
            field=models.ForeignKey(db_column='indic_incid_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_indicateur', to='Mapapi.indicateur'),
        ),
        migrations.AddField(
            model_name='incident',
            name='taken_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taken_incidents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incident',
            name='user_id',
            field=models.ForeignKey(db_column='user_incid_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_incident', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evenement',
            name='user_id',
            field=models.ForeignKey(db_column='user_event_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='communaute',
            name='zone',
            field=models.ForeignKey(db_column='zone_communaute_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Zone_communaute', to='Mapapi.zone'),
        ),
        migrations.AddField(
            model_name='collaboration',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mapapi.incident'),
        ),
        migrations.AddField(
            model_name='collaboration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Colaboration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField()),
                ('motivation', models.TextField(blank=True, null=True)),
                ('other_option', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mapapi.incident')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

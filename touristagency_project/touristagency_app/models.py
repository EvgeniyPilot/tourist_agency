# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Clients(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clients'


class Countrys(models.Model):
    namecountry = models.CharField(db_column='nameCountry', max_length=50)  # Field name made lowercase.
    tour = models.ForeignKey('Tours', models.DO_NOTHING, db_column='idTour')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countrys'


class Employees(models.Model):
    nameemploy = models.CharField(db_column='nameEmploy', max_length=50)  # Field name made lowercase.
    post = models.ForeignKey('Posts', models.DO_NOTHING, db_column='idPost')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'


class Hotels(models.Model):
    namehotel = models.CharField(db_column='nameHotel', max_length=50)  # Field name made lowercase.
    addresshotel = models.CharField(db_column='addressHotel', max_length=50)  # Field name made lowercase.
    tour = models.ForeignKey('Tours', models.DO_NOTHING, db_column='idTour')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotels'


class Posts(models.Model):
    namepost = models.CharField(db_column='namePost', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.namepost

    class Meta:
        managed = False
        db_table = 'posts'


class Sales(models.Model):
    cost = models.IntegerField()
    client = models.ForeignKey(Clients, models.DO_NOTHING, db_column='idClient')  # Field name made lowercase.
    tour = models.ForeignKey('Tours', models.DO_NOTHING, db_column='idTour')  # Field name made lowercase.
    employ = models.ForeignKey(Employees, models.DO_NOTHING, db_column='idEmploy', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales'


class Tours(models.Model):
    nametour = models.CharField(db_column='nameTour', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tours'

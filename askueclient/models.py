# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Data1H(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dtime = models.DateTimeField()
    point = models.IntegerField()
    param = models.IntegerField()
    zn = models.FloatField()

    class Meta:
        managed = False
        db_table = 'data_1h'


class Data30M(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dtime = models.DateTimeField()
    point = models.IntegerField()
    param = models.IntegerField()
    zn = models.FloatField()

    class Meta:
        managed = False
        db_table = 'data_30m'


class Data5M(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dtime = models.DateTimeField()
    point = models.IntegerField()
    param = models.IntegerField()
    zn = models.FloatField()

    class Meta:
        managed = False
        db_table = 'data_5m'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'groups'


class Point(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    obj = models.IntegerField()
    name = models.CharField(max_length=80)
    klass_u = models.IntegerField()
    group = models.ForeignKey(Groups, db_column='group', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'point'


class Point_kp(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    point = models.IntegerField()
    kp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'point_kp'


class TimeDay(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number_3min = models.CharField(db_column='3min', max_length=30, blank=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5min = models.CharField(db_column='5min', max_length=30, blank=True)  # Field renamed because it wasn't a valid Python identifier.
    number_30min = models.CharField(db_column='30min', max_length=30, blank=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1hour = models.CharField(db_column='1hour', max_length=30, blank=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'time_day'


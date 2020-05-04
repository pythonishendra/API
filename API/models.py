# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address_line1 = models.CharField(max_length=250)
    address_line2 = models.CharField(max_length=250)
    city = models.IntegerField()
    img = models.CharField(max_length=250)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'address'


class AdminDetails(models.Model):
    mobile = models.CharField(db_column='Mobile', max_length=15)  # Field name made lowercase.
    #image = models.CharField(db_column='Image', max_length=250)  # Field name made lowercase.
    image=models.FileField(upload_to='media')
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_details'


class AdminPasswordRecovery(models.Model):
    uniquid = models.CharField(db_column='UniquId', max_length=100)  # Field name made lowercase.
    otp = models.CharField(db_column='Otp', max_length=20)  # Field name made lowercase.
    requesttime = models.DateTimeField(db_column='RequestTime')  # Field name made lowercase.
    userid = models.ForeignKey('TblAdmin', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_password_recovery'


class AreaOfInterest(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    interest = models.CharField(db_column='Interest', max_length=200)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'area_of_interest'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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


class City(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=100)  # Field name made lowercase.
    citycode = models.CharField(db_column='CityCode', max_length=50)  # Field name made lowercase.
    stateid = models.IntegerField(db_column='StateId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=100)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=50)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


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

from datetime import datetime    

class Eligibilitycheckedmember(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=250)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250,null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=200,null=True)  # Field name made lowercase.
    dates = models.DateTimeField(db_column='Dates',default=datetime.now)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eligibilitycheckedmember'


class Location(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'location'


class MemberAddress(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=200)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=200)  # Field name made lowercase.
    country = models.IntegerField(db_column='Country')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    city = models.IntegerField(db_column='City')  # Field name made lowercase.
    pincode = models.BigIntegerField(db_column='PinCode')  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_address'


class MemberDetails(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    occupassionid = models.IntegerField(db_column='OccupassionId', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=20, blank=True, null=True)  # Field name made lowercase.
    merital_status = models.IntegerField(db_column='Merital_Status', blank=True, null=True)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='Dob', blank=True, null=True)  # Field name made lowercase.
    anual_income = models.FloatField(db_column='Anual_Income', blank=True, null=True)  # Field name made lowercase.
    rashancardtype = models.CharField(db_column='RashanCardType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    physicallychalenged = models.IntegerField(db_column='PhysicallyChalenged', blank=True, null=True)  # Field name made lowercase.
    areaofinterest = models.IntegerField(db_column='AreaOfInterest', blank=True, null=True)  # Field name made lowercase.
    skills = models.IntegerField(db_column='Skills', blank=True, null=True)  # Field name made lowercase.
    locality = models.CharField(db_column='Locality', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_details'


class MemberPasswordRecovery(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    otp = models.CharField(db_column='Otp', max_length=10)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='UniqueId', max_length=100)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberId')  # Field name made lowercase.
    requesttime = models.DateTimeField(db_column='RequestTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_password_recovery'


class MemberWorkExperience(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    year_of_exp = models.IntegerField(db_column='Year_Of_Exp', blank=True, null=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='Org_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    district = models.IntegerField(db_column='District', blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=15, blank=True, null=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_work_experience'


class MeritalStatus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    merital_status = models.CharField(db_column='Merital_Status', max_length=100)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merital_status'


class MultiCate(models.Model):
    scheme_id = models.IntegerField()
    occupation_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'multi_cate'


class Occupation(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'occupation'


class Organization(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    organization_name = models.CharField(db_column='Organization_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    head_of_organization = models.CharField(db_column='Head_Of_Organization', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type_of_organization = models.CharField(db_column='Type_Of_Organization', max_length=100, blank=True, null=True)  # Field name made lowercase.
    registration_number = models.CharField(db_column='Registration_Number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    why_you_join = models.CharField(db_column='Why_You_Join', max_length=200, blank=True, null=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='Member_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organization'


class Pages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    page_name = models.CharField(db_column='Page_Name', max_length=200)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150)  # Field name made lowercase.
    sortdesc = models.CharField(db_column='SortDesc', max_length=250)  # Field name made lowercase.
    longdesc = models.CharField(db_column='LongDesc', max_length=500)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=250)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pages'


class Photo(models.Model):
    name = models.CharField(max_length=250)
    cate_id = models.IntegerField()
    img = models.CharField(max_length=250)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photo'


class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    p_desc = models.TextField()
    status = models.IntegerField()
    cate = models.IntegerField()
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class ProjectCate(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_cate'


class Reports(models.Model):
    name = models.CharField(max_length=100)
    pdf = models.CharField(max_length=250)
    img = models.CharField(max_length=250)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reports'


class SCategory(models.Model):
    s_name = models.CharField(max_length=250)
    s_img = models.CharField(max_length=250)
    s_type = models.IntegerField()
    s_state = models.IntegerField()
    s_short_desc = models.CharField(max_length=250)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 's_category'


class Schemeapplied(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schemeid = models.IntegerField(db_column='SChemeId')  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberId')  # Field name made lowercase.
    applieddate = models.DateTimeField(db_column='AppliedDate')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schemeapplied'


class SchemesDetails(models.Model):
    scheme_id = models.IntegerField(db_column='Scheme_Id')  # Field name made lowercase.
    scheme_desc = models.TextField()
    eligibility_desc = models.TextField()
    benifits_desc = models.TextField()
    mode_desc = models.TextField()
    requireddocument = models.CharField(db_column='RequiredDocument', max_length=250)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schemes_details'


class Schems(models.Model):
    p_cate = models.IntegerField()
    scheme_name = models.CharField(max_length=100)
    s_desc = models.CharField(max_length=250)
    upload_img = models.FileField(upload_to='media')
    s_type = models.IntegerField()
    scheme_for = models.CharField(max_length=100)
    marriage = models.CharField(max_length=250)
    scheme_age = models.CharField(max_length=250)
    family_income = models.CharField(max_length=100)
    b_category = models.CharField(max_length=11)
    divyang = models.CharField(max_length=11)
    s_state = models.IntegerField()
    occupation = models.CharField(max_length=250)
    scheme_for_locality = models.CharField(db_column='Scheme_For_Locality', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s_category = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schems'


class Skills(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    skill = models.CharField(db_column='Skill', max_length=200)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skills'


class State(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100)  # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=100)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'state'


class TblAdmin(models.Model):
    userid = models.CharField(db_column='UserId', unique=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_admin'


class TblDonation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    amount = models.BigIntegerField(db_column='Amount')  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberId')  # Field name made lowercase.
    membertype = models.IntegerField(db_column='MemberType')  # Field name made lowercase.
    donationdate = models.DateTimeField(db_column='DonationDate')  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=100)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_donation'


class TblMember(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    f_name = models.CharField(db_column='F_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15)  # Field name made lowercase.
    mobile_isverified = models.IntegerField(db_column='Mobile_IsVerified')  # Field name made lowercase.
    member_type = models.IntegerField(db_column='Member_Type')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_On')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_member'


class TblMemberType(models.Model):
    membertype = models.CharField(db_column='MemberType', max_length=200)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_member_type'


class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    team_desc = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team'


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_member'


class Video(models.Model):
    url = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    cat_id = models.IntegerField()
    sceme_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'video'


class Workinfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    organizationname = models.CharField(db_column='OrganizationName', max_length=200)  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    district = models.IntegerField(db_column='District')  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=100)  # Field name made lowercase.
    comment = models.IntegerField(db_column='Comment')  # Field name made lowercase.
    member_id = models.IntegerField(db_column='Member_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workinfo'

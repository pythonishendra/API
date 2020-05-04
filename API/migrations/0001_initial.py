# Generated by Django 3.0.5 on 2020-05-04 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=250)),
                ('address_line2', models.CharField(max_length=250)),
                ('city', models.IntegerField()),
                ('img', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdminDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(db_column='Mobile', max_length=15)),
                ('image', models.FileField(upload_to='media')),
            ],
            options={
                'db_table': 'admin_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdminPasswordRecovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniquid', models.CharField(db_column='UniquId', max_length=100)),
                ('otp', models.CharField(db_column='Otp', max_length=20)),
                ('requesttime', models.DateTimeField(db_column='RequestTime')),
            ],
            options={
                'db_table': 'admin_password_recovery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('interest', models.CharField(db_column='Interest', max_length=200)),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'area_of_interest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('cityname', models.CharField(db_column='CityName', max_length=100)),
                ('citycode', models.CharField(db_column='CityCode', max_length=50)),
                ('stateid', models.IntegerField(db_column='StateId')),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('countryname', models.CharField(db_column='CountryName', max_length=100)),
                ('countrycode', models.CharField(db_column='CountryCode', max_length=50)),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eligibilitycheckedmember',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=250)),
                ('email', models.CharField(db_column='Email', max_length=250)),
                ('mobile', models.CharField(db_column='Mobile', max_length=20)),
                ('gender', models.CharField(db_column='Gender', max_length=100)),
                ('address', models.CharField(db_column='Address', max_length=250, null=True)),
                ('location', models.CharField(db_column='Location', max_length=200, null=True)),
                ('dates', models.DateTimeField(db_column='Dates', default=datetime.datetime.now)),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'eligibilitycheckedmember',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('l_id', models.AutoField(primary_key=True, serialize=False)),
                ('l_name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberAddress',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('address1', models.CharField(db_column='Address1', max_length=200)),
                ('address2', models.CharField(db_column='Address2', max_length=200)),
                ('country', models.IntegerField(db_column='Country')),
                ('state', models.IntegerField(db_column='State')),
                ('city', models.IntegerField(db_column='City')),
                ('pincode', models.BigIntegerField(db_column='PinCode')),
                ('area', models.CharField(blank=True, db_column='Area', max_length=200, null=True)),
                ('memberid', models.IntegerField(db_column='MemberId')),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'member_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberDetails',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('occupassionid', models.IntegerField(blank=True, db_column='OccupassionId', null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=20, null=True)),
                ('merital_status', models.IntegerField(blank=True, db_column='Merital_Status', null=True)),
                ('qualification', models.CharField(blank=True, db_column='Qualification', max_length=200, null=True)),
                ('dob', models.DateField(blank=True, db_column='Dob', null=True)),
                ('anual_income', models.FloatField(blank=True, db_column='Anual_Income', null=True)),
                ('rashancardtype', models.CharField(blank=True, db_column='RashanCardType', max_length=100, null=True)),
                ('physicallychalenged', models.IntegerField(blank=True, db_column='PhysicallyChalenged', null=True)),
                ('areaofinterest', models.IntegerField(blank=True, db_column='AreaOfInterest', null=True)),
                ('skills', models.IntegerField(blank=True, db_column='Skills', null=True)),
                ('locality', models.CharField(blank=True, db_column='Locality', max_length=200, null=True)),
                ('comment', models.CharField(blank=True, db_column='Comment', max_length=250, null=True)),
                ('memberid', models.IntegerField(blank=True, db_column='MemberId', null=True)),
            ],
            options={
                'db_table': 'member_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberPasswordRecovery',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('otp', models.CharField(db_column='Otp', max_length=10)),
                ('uniqueid', models.CharField(db_column='UniqueId', max_length=100)),
                ('memberid', models.IntegerField(db_column='MemberId')),
                ('requesttime', models.DateTimeField(db_column='RequestTime')),
            ],
            options={
                'db_table': 'member_password_recovery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberWorkExperience',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('year_of_exp', models.IntegerField(blank=True, db_column='Year_Of_Exp', null=True)),
                ('org_name', models.CharField(blank=True, db_column='Org_Name', max_length=100, null=True)),
                ('state', models.IntegerField(blank=True, db_column='State', null=True)),
                ('district', models.IntegerField(blank=True, db_column='District', null=True)),
                ('website', models.CharField(blank=True, db_column='Website', max_length=100, null=True)),
                ('contact', models.CharField(blank=True, db_column='Contact', max_length=15, null=True)),
                ('memberid', models.IntegerField(blank=True, db_column='MemberId', null=True)),
            ],
            options={
                'db_table': 'member_work_experience',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MeritalStatus',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('merital_status', models.CharField(db_column='Merital_Status', max_length=100)),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'merital_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MultiCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_id', models.IntegerField()),
                ('occupation_id', models.IntegerField()),
            ],
            options={
                'db_table': 'multi_cate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'occupation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('organization_name', models.CharField(blank=True, db_column='Organization_Name', max_length=100, null=True)),
                ('head_of_organization', models.CharField(blank=True, db_column='Head_Of_Organization', max_length=200, null=True)),
                ('type_of_organization', models.CharField(blank=True, db_column='Type_Of_Organization', max_length=100, null=True)),
                ('registration_number', models.CharField(blank=True, db_column='Registration_Number', max_length=100, null=True)),
                ('why_you_join', models.CharField(blank=True, db_column='Why_You_Join', max_length=200, null=True)),
                ('member_id', models.IntegerField(db_column='Member_Id')),
            ],
            options={
                'db_table': 'organization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('page_name', models.CharField(db_column='Page_Name', max_length=200)),
                ('title', models.CharField(db_column='Title', max_length=150)),
                ('sortdesc', models.CharField(db_column='SortDesc', max_length=250)),
                ('longdesc', models.CharField(db_column='LongDesc', max_length=500)),
                ('image', models.CharField(db_column='Image', max_length=250)),
                ('createdon', models.DateTimeField(db_column='CreatedOn')),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'pages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cate_id', models.IntegerField()),
                ('img', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('p_desc', models.TextField()),
                ('status', models.IntegerField()),
                ('cate', models.IntegerField()),
                ('createdon', models.DateTimeField(db_column='CreatedOn')),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('createdon', models.DateTimeField(db_column='CreatedOn')),
            ],
            options={
                'db_table': 'project_cate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pdf', models.CharField(max_length=250)),
                ('img', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'reports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=250)),
                ('s_img', models.CharField(max_length=250)),
                ('s_type', models.IntegerField()),
                ('s_state', models.IntegerField()),
                ('s_short_desc', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 's_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schemeapplied',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('schemeid', models.IntegerField(db_column='SChemeId')),
                ('memberid', models.IntegerField(db_column='MemberId')),
                ('applieddate', models.DateTimeField(db_column='AppliedDate')),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'schemeapplied',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchemesDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_id', models.IntegerField(db_column='Scheme_Id')),
                ('scheme_desc', models.TextField()),
                ('eligibility_desc', models.TextField()),
                ('benifits_desc', models.TextField()),
                ('mode_desc', models.TextField()),
                ('requireddocument', models.CharField(db_column='RequiredDocument', max_length=250)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'schemes_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_cate', models.IntegerField()),
                ('scheme_name', models.CharField(max_length=100)),
                ('s_desc', models.CharField(max_length=250)),
                ('upload_img', models.FileField(upload_to='media')),
                ('s_type', models.IntegerField()),
                ('scheme_for', models.CharField(max_length=100)),
                ('marriage', models.CharField(max_length=250)),
                ('scheme_age', models.CharField(max_length=250)),
                ('family_income', models.CharField(max_length=100)),
                ('b_category', models.CharField(max_length=11)),
                ('divyang', models.CharField(max_length=11)),
                ('s_state', models.IntegerField()),
                ('occupation', models.CharField(max_length=250)),
                ('scheme_for_locality', models.CharField(blank=True, db_column='Scheme_For_Locality', max_length=200, null=True)),
                ('s_category', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'schems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('skill', models.CharField(db_column='Skill', max_length=200)),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'skills',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('statename', models.CharField(db_column='StateName', max_length=100)),
                ('statecode', models.CharField(db_column='StateCode', max_length=100)),
                ('countryid', models.IntegerField(db_column='CountryId')),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(db_column='UserId', max_length=100, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=100)),
            ],
            options={
                'db_table': 'tbl_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblDonation',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('amount', models.BigIntegerField(db_column='Amount')),
                ('memberid', models.IntegerField(db_column='MemberId')),
                ('membertype', models.IntegerField(db_column='MemberType')),
                ('donationdate', models.DateTimeField(db_column='DonationDate')),
                ('paymentmethod', models.CharField(db_column='PaymentMethod', max_length=100)),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'tbl_donation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('f_name', models.CharField(blank=True, db_column='F_Name', max_length=100, null=True)),
                ('email', models.CharField(db_column='Email', max_length=100)),
                ('mobile', models.CharField(db_column='Mobile', max_length=15)),
                ('mobile_isverified', models.IntegerField(db_column='Mobile_IsVerified')),
                ('member_type', models.IntegerField(db_column='Member_Type')),
                ('createdby', models.IntegerField(blank=True, db_column='CreatedBy', null=True)),
                ('created_on', models.DateTimeField(db_column='Created_On')),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'tbl_member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membertype', models.CharField(db_column='MemberType', max_length=200)),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'tbl_member_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=100)),
                ('team_desc', models.TextField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'team_member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('cat_id', models.IntegerField()),
                ('sceme_id', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'video',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workinfo',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('organizationname', models.CharField(db_column='OrganizationName', max_length=200)),
                ('state', models.IntegerField(db_column='State')),
                ('district', models.IntegerField(db_column='District')),
                ('website', models.CharField(db_column='Website', max_length=100)),
                ('comment', models.IntegerField(db_column='Comment')),
                ('member_id', models.IntegerField(db_column='Member_Id')),
            ],
            options={
                'db_table': 'workinfo',
                'managed': False,
            },
        ),
    ]

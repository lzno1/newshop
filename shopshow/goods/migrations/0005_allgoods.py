# Generated by Django 3.1.3 on 2023-03-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_caigou'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_Product_Name', models.CharField(blank=True, max_length=80, null=True)),
                ('base_Product_Number', models.CharField(blank=True, max_length=10, null=True)),
                ('base_Product_IsHazmat', models.CharField(blank=True, max_length=20, null=True)),
                ('base_Description', models.CharField(blank=True, max_length=1000, null=True)),
                ('base_Summary', models.CharField(blank=True, max_length=80, null=True)),
                ('base_Product_Type', models.CharField(blank=True, max_length=80, null=True)),
                ('base_Category', models.CharField(blank=True, max_length=300, null=True)),
                ('base_Keywords', models.CharField(blank=True, max_length=300, null=True)),
                ('base_Product_Color', models.CharField(blank=True, max_length=500, null=True)),
                ('base_Material', models.CharField(blank=True, max_length=100, null=True)),
                ('base_Size_Group', models.CharField(blank=True, max_length=80, null=True)),
                ('base_Size_Values', models.CharField(blank=True, max_length=80, null=True)),
                ('base_Shape', models.CharField(blank=True, max_length=80, null=True)),
                ('base_Theme', models.CharField(blank=True, max_length=80, null=True)),
                ('imprint_Origin', models.CharField(blank=True, max_length=80, null=True)),
                ('imprint_Imprint_Method', models.CharField(blank=True, max_length=80, null=True)),
                ('imprint_Imprint_Color', models.CharField(blank=True, max_length=80, null=True)),
                ('imprint_Imprint_Size', models.CharField(blank=True, max_length=80, null=True)),
                ('imprint_Imprint_Location', models.CharField(blank=True, max_length=80, null=True)),
                ('imprint_Price_Includes', models.CharField(blank=True, max_length=80, null=True)),
                ('imprint_Sequence', models.CharField(blank=True, max_length=4, null=True)),
                ('imprint_Currency', models.CharField(blank=True, max_length=3, null=True)),
                ('imprint_Always_Free_Setup', models.CharField(blank=True, max_length=3, null=True)),
                ('imprint_Upcharge_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('imprint_Upcharge_Criteria_1', models.CharField(blank=True, max_length=30, null=True)),
                ('imprint_Upcharge_Criteria_2', models.CharField(blank=True, max_length=30, null=True)),
                ('imprint_Upcharge_Type', models.CharField(blank=True, max_length=20, null=True)),
                ('imprint_Upcharge_Level', models.CharField(blank=True, max_length=20, null=True)),
                ('imprint_Service_Charge', models.CharField(blank=True, max_length=20, null=True)),
                ('imprint_UQ1', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ2', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ3', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ4', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ5', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ6', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ7', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ8', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ9', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UQ10', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP1', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP2', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP3', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP4', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP5', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP6', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP7', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP8', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP9', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UP10', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD1', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD2', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD3', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD4', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD5', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD6', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD7', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD8', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD9', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_UD10', models.CharField(blank=True, max_length=6, null=True)),
                ('imprint_Upcharge_Details', models.CharField(blank=True, max_length=80, null=True)),
                ('PS_Production_Time', models.CharField(blank=True, max_length=20, null=True)),
                ('PS_Rush_Service', models.CharField(blank=True, max_length=10, null=True)),
                ('PS_Rush_Time', models.CharField(blank=True, max_length=20, null=True)),
                ('PS_Same_Day_Service', models.CharField(blank=True, max_length=20, null=True)),
                ('PS_Packaging', models.CharField(blank=True, max_length=40, null=True)),
                ('PS_Shipping_Items', models.CharField(blank=True, max_length=40, null=True)),
                ('PS_Shipping_Dimensions', models.CharField(blank=True, max_length=40, null=True)),
                ('PS_Shipping_Weight', models.CharField(blank=True, max_length=40, null=True)),
                ('PS_Shipper_Bills_By', models.CharField(blank=True, max_length=20, null=True)),
                ('PS_Shipping_Info', models.CharField(blank=True, max_length=40, null=True)),
                ('PS_Free_Shipping', models.CharField(blank=True, max_length=4, null=True)),
                ('QPD_Q1', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q2', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q3', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q4', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q5', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q6', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q7', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q8', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q9', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_Q10', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P1', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P2', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P3', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P4', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P5', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P6', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P7', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P8', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P9', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_P10', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D1', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D2', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D3', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D4', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D5', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D6', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D7', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D8', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D9', models.CharField(blank=True, max_length=8, null=True)),
                ('QPD_D10', models.CharField(blank=True, max_length=8, null=True)),
                ('other_Carrier_Information', models.CharField(blank=True, max_length=100, null=True)),
                ('other_Market_Segment', models.CharField(blank=True, max_length=40, null=True)),
                ('other_Distributor_View_Only', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]

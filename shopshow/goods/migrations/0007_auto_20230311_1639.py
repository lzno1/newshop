# Generated by Django 3.1.3 on 2023-03-11 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20230311_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Always_Free_Setup',
            new_name='Always_Free_Setup',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Material',
            new_name='Carrier_Information',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Currency',
            new_name='Currency',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Free_Shipping',
            new_name='Distributor_View_Only',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Sequence',
            new_name='Free_Shipping',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Product_Name',
            new_name='Imprint_Color',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Product_Type',
            new_name='Imprint_Location',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Shape',
            new_name='Imprint_Method',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Size_Group',
            new_name='Imprint_Size',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Keywords',
            new_name='Keywords',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Packaging',
            new_name='Market_Segment',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='other_Carrier_Information',
            new_name='Material',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Size_Values',
            new_name='Origin',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Shipping_Dimensions',
            new_name='Packaging',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Summary',
            new_name='Price_Includes',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Product_Color',
            new_name='Product_Color',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Production_Time',
            new_name='Product_IsHazmat',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Theme',
            new_name='Product_Name',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Rush_Service',
            new_name='Product_Number',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Imprint_Color',
            new_name='Product_Type',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Rush_Time',
            new_name='Production_Time',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Product_Number',
            new_name='Rush_Service',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Shipper_Bills_By',
            new_name='Rush_Time',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Same_Day_Service',
            new_name='Same_Day_Service',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='other_Distributor_View_Only',
            new_name='Sequence',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='base_Product_IsHazmat',
            new_name='Service_Charge',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Imprint_Location',
            new_name='Shape',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Service_Charge',
            new_name='Shipper_Bills_By',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Shipping_Info',
            new_name='Shipping_Dimensions',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Shipping_Items',
            new_name='Shipping_Info',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='PS_Shipping_Weight',
            new_name='Shipping_Items',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='other_Market_Segment',
            new_name='Shipping_Weight',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Imprint_Method',
            new_name='Size_Group',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Imprint_Size',
            new_name='Size_Values',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Origin',
            new_name='Summary',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Upcharge_Details',
            new_name='Theme',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Upcharge_Criteria_1',
            new_name='Upcharge_Criteria_1',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Upcharge_Criteria_2',
            new_name='Upcharge_Criteria_2',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Price_Includes',
            new_name='Upcharge_Details',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Upcharge_Level',
            new_name='Upcharge_Level',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Upcharge_Name',
            new_name='Upcharge_Name',
        ),
        migrations.RenameField(
            model_name='allgoods',
            old_name='imprint_Upcharge_Type',
            new_name='Upcharge_Type',
        ),
    ]

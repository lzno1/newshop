from django.shortcuts import render
from .models import ALLHotGoods
from .models import Dingdans
from .models import AllGoods
import csv

# Create your views here.
def goods(request):
    allhotgoods = ALLHotGoods.objects.all()
    return render(request, 'goods.html', {'hotgoods': allhotgoods})

def dingdans(request):
    dingdan = Dingdans.objects.all()
    return render(request, 'goods.html', {'dingdan': dingdan})

def allgoods(request):
    if request.POST:
        if 'save' in request.POST:
            # try:
            Product_Name = request.POST['Product_Name']
            Product_Number = request.POST['Product_Number']
            Product_IsHazmat = request.POST['Product_IsHazmat']
            Description = request.POST['Description']
            Summary = request.POST['Summary']
            Product_Type = request.POST['Product_Type']
            Category = request.POST['Category']
            Keywords = request.POST['Keywords']
            Product_Color = request.POST['Product_Color']
            Material = request.POST['Material']
            Size_Group = request.POST['Size_Group']
            Size_Values = request.POST['Size_Values']
            Shape = request.POST['Shape']
            Theme = request.POST['Theme']

            Origin = request.POST['Origin']
            Imprint_Method = request.POST['Imprint_Method']
            Imprint_Color = request.POST['Imprint_Color']
            Imprint_Size = request.POST['Imprint_Size']
            Imprint_Location = request.POST['Imprint_Location']
            Price_Includes = request.POST['Price_Includes']
            Sequence = request.POST['Sequence']
            Currency = request.POST['Currency']
            Always_Free_Setup = request.POST['Always_Free_Setup']
            Upcharge_Name = request.POST['Upcharge_Name']
            Upcharge_Criteria_1 = request.POST['Upcharge_Criteria_1']
            Upcharge_Criteria_2 = request.POST['Upcharge_Criteria_2']
            Upcharge_Type = request.POST['Upcharge_Type']
            Upcharge_Level = request.POST['Upcharge_Level']
            Service_Charge = request.POST['Service_Charge']
            UQ1 = request.POST['UQ1']
            UQ2 = request.POST['UQ2']
            UQ3 = request.POST['UQ3']
            UQ4 = request.POST['UQ4']
            UQ5 = request.POST['UQ5']
            UQ6 = request.POST['UQ6']
            UQ7 = request.POST['UQ7']
            UQ8 = request.POST['UQ8']
            UQ9 = request.POST['UQ9']
            UQ10 = request.POST['UQ10']
            UP1 = request.POST['UP1']
            UP2 = request.POST['UP2']
            UP3 = request.POST['UP3']
            UP4 = request.POST['UP4']
            UP5 = request.POST['UP5']
            UP6 = request.POST['UP6']
            UP7 = request.POST['UP7']
            UP8 = request.POST['UP8']
            UP9 = request.POST['UP9']
            UP10 = request.POST['UP10']
            UD1 = request.POST['UD1']
            UD2 = request.POST['UD2']
            UD3 = request.POST['UD3']
            UD4 =request.POST['UD4']
            UD5 =request.POST['UD5']
            UD6 = request.POST['UD6']
            UD7 = request.POST['UD7']
            UD8 = request.POST['UD8']
            UD9 = request.POST['UD9']
            UD10 = request.POST['UD10']
            Upcharge_Details = request.POST['Upcharge_Details']
            

            Production_Time = request.POST['Production_Time']
            Rush_Service = request.POST['Rush_Service']
            Rush_Time = request.POST['Rush_Time']
            Same_Day_Service = request.POST['Same_Day_Service']
            Packaging = request.POST['Packaging']
            Shipping_Items = request.POST['Shipping_Items']
            Shipping_Dimensions = request.POST['Shipping_Dimensions']
            Shipping_Weight = request.POST['Shipping_Weight']
            Shipper_Bills_By = request.POST['Shipper_Bills_By']
            Shipping_Info = request.POST['Shipping_Info']
            Free_Shipping =request.POST['Free_Shipping']


            Q1 = request.POST['Q1']
            Q2 = request.POST['Q2']
            Q3 = request.POST['Q3']
            Q4 = request.POST['Q4']
            Q5 = request.POST['Q5']
            Q6 = request.POST['Q6']
            Q7 = request.POST['Q7']
            Q8 = request.POST['Q8']
            Q9 = request.POST['Q9']
            Q10 = request.POST['Q10']
            P1 = request.POST['P1']
            P2 = request.POST['P2']
            P3 = request.POST['P3']
            P4 = request.POST['P4']
            P5 = request.POST['P5']
            P6 = request.POST['P6']
            P7 = request.POST['P7']
            P8 = request.POST['P8']
            P9 = request.POST['P9']
            P10 = request.POST['P10']
            D1 = request.POST['D1']
            D2 = request.POST['D2']
            D3 = request.POST['D3']
            D4 = request.POST['D4']
            D5 = request.POST['D5']
            D6 = request.POST['D6']
            D7 = request.POST['D7']
            D8 = request.POST['D8']
            D9 = request.POST['D9']
            D10 = request.POST['D10']

            Distributor_View_Only = request.POST['Distributor_View_Only']
            Carrier_Information = request.POST['Carrier_Information']
            Market_Segment = request.POST['Market_Segment']
            AllGoods.objects.create(Product_Name=Product_Name, Product_Number=Product_Number, Product_IsHazmat=Product_IsHazmat, Description=Description, Summary=Summary, Product_Type=Product_Type, Category=Category, Keywords=Keywords, Product_Color=Product_Color, Material=Material, Size_Group=Size_Group, Size_Values=Size_Values, Shape=Shape, Theme=Theme, Origin=Origin, Imprint_Method=Imprint_Method, Imprint_Color=Imprint_Color, Imprint_Size=Imprint_Size, Imprint_Location=Imprint_Location, Price_Includes=Price_Includes, Sequence=Sequence, Currency=Currency, Always_Free_Setup=Always_Free_Setup, Upcharge_Name=Upcharge_Name, Upcharge_Criteria_1=Upcharge_Criteria_1, Upcharge_Criteria_2=Upcharge_Criteria_2, Upcharge_Type=Upcharge_Type, Upcharge_Level=Upcharge_Level, Service_Charge=Service_Charge, UQ1=UQ1, UQ2=UQ2, UQ3=UQ3, UQ4=UQ4, UQ5=UQ5, UQ6=UQ6, UQ7=UQ7, UQ8=UQ8, UQ9=UQ9, UQ10=UQ10, UP1=UP1, UP2=UP2, UP3=UP3, UP4=UP4, UP5=UP5, UP6=UP6, UP7=UP7, UP8=UP8, UP9=UP9, UP10=UP10, UD1=UD1, UD2=UD2, UD3=UD3, UD4=UD4, UD5=UD5, UD6=UD6, UD7=UD7, UD8=UD8, UD9=UD9, UD10=UD10, Upcharge_Details=Upcharge_Details, Production_Time=Production_Time, Rush_Service=Rush_Service, Rush_Time=Rush_Time, Same_Day_Service=Same_Day_Service, Packaging=Packaging, Shipping_Items=Shipping_Items, Shipping_Dimensions=Shipping_Dimensions, Shipping_Weight=Shipping_Weight, Shipper_Bills_By=Shipper_Bills_By, Shipping_Info=Shipping_Info, Free_Shipping=Free_Shipping, Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5, Q6=Q6, Q7=Q7, Q8=Q8, Q9=Q9, Q10=Q10, P1=P1, P2=P2, P3=P3, P4=P4, P5=P5, P6=P6, P7=P7, P8=P8, P9=P9, P10=P10, D1=D1, D2=D2, D3=D3, D4=D4, D5=D5, D6=D6, D7=D7, D8=D8, D9=D9, D10=D10, Distributor_View_Only=Distributor_View_Only, Carrier_Information=Carrier_Information, Market_Segment=Market_Segment)
            return render(request, 'UploadGoods.html', {'logging':'成功保存订单'})
            # except:
            #     return render(request, 'UploadGoods.html', {'logging':'未能成功保存商品信息'})
        elif 'search' in request.POST:
            try:
                good_id = request.POST['Product_Number']
                good_info = AllGoods.objects.get(Product_Number = good_id)
                if good_info:
                    return render(request, 'UploadGoods.html', {'good_info':good_info,'logging':'已查询到对应商品'})
            except:
                return render(request, 'UploadGoods.html', {'logging':'未能查询到id对应商品'})
        elif 'del' in request.POST:
            try:
                goodid = request.POST['Product_Number']
                AllGoods.objects.filter(Product_Number=goodid).delete()
                return render(request, 'UploadGoods.html', {'logging':'成功删除商品信息'})
            except:
                return render(request, 'UploadGoods.html', {'logging':'未能成功删除商品信息'})
        elif 'new' in request.POST:
            # data = getdata('F:\第一人生\软件设计--外接\外贸网站\c46671已修改.csv')
            # for one in data:
            #     try:
            #         AllGoods.objects.create(Product_Name=one[0], Product_Number=one[1],Product_img=one[2], Product_IsHazmat=one[3], Description=one[4], Summary=one[5], Product_Type=one[6], Category=one[7], Keywords=one[8], Product_Color=one[9], Material=one[10], Size_Group=one[11], Size_Values=one[12], Shape=one[13], Theme=one[14], Origin=one[15], Imprint_Method=one[16], Imprint_Color=one[17], Imprint_Size=one[18], Imprint_Location=one[19], Price_Includes=one[20], Sequence=one[21], Currency=one[22], Always_Free_Setup=one[23], Upcharge_Name=one[24], Upcharge_Criteria_1=one[25], Upcharge_Criteria_2=one[26], Upcharge_Type=one[27], Upcharge_Level=one[28], Service_Charge=one[29], UQ1=one[30], UQ2=one[31], UQ3=one[32], UQ4=one[33], UQ5=one[34], UQ6=one[35], UQ7=one[36], UQ8=one[37], UQ9=one[38], UQ10=one[39], UP1=one[40], UP2=one[41], UP3=one[42], UP4=one[43], UP5=one[44], UP6=one[45], UP7=one[46], UP8=one[47], UP9=one[48], UP10=one[49], UD1=one[50], UD2=one[51], UD3=one[52], UD4=one[53], UD5=one[54], UD6=one[55], UD7=one[56], UD8=one[57], UD9=one[58], UD10=one[59], Upcharge_Details=one[60], Production_Time=one[61], Rush_Service=one[62], Rush_Time=one[63], Same_Day_Service=one[64], Packaging=one[65], Shipping_Items=one[66], Shipping_Dimensions=one[67], Shipping_Weight=one[68], Shipper_Bills_By=one[69], Shipping_Info=one[70], Free_Shipping=one[71], Q1=one[72], Q2=one[73], Q3=one[74], Q4=one[75], Q5=one[76], Q6=one[77], Q7=one[78], Q8=one[79], Q9=one[80], Q10=one[81], P1=one[82], P2=one[83], P3=one[84], P4=one[85], P5=one[86], P6=one[87], P7=one[88], P8=one[89], P9=one[90], P10=one[91], D1=one[92], D2=one[93], D3=one[94], D4=one[95], D5=one[96], D6=one[97], D7=one[98], D8=one[99], D9=one[100], D10=one[101], Distributor_View_Only=one[102], Carrier_Information=one[103], Market_Segment=one[104])
            #     except:
            #         pass
            try:
                goodid = request.POST['Product_Number']
                AllGoods.objects.create(Product_Number=goodid)
                good_info = AllGoods.objects.get(Product_Number = goodid)
                return render(request, 'UploadGoods.html', {'good_info':good_info,'logging':'新建商品信息'})
            except:
                return render(request, 'UploadGoods.html', {'logging':'新建商品信息失败'})
    return render(request, 'UploadGoods.html')


def showAllGood(request):
    allgoods = AllGoods.objects.all()[:100]
    return render(request, 'goods.html', {'goods': allgoods})

def goodInfo(request, goodid):
    id = goodid
    goodinfo = AllGoods.objects.filter(Product_Number = id).first()
    print(goodinfo.Product_Number)
    return render(request, 'goodinfo.html', {'info': goodinfo})


def getdata(filepath):
    data = []
    with open(filepath, 'rt') as f:
        lines = csv.reader(f)
        for line in lines:
            data.append(line)

    new_data = []
    for one in data[1:]:
        add_data = []
        add_data.append(one[1])
        add_data.append(one[2])
        add_data.append('../static/img/goods/' + one[2] + '.jpg')
        add_data.append(one[8])
        add_data.append(one[10])
        add_data.append(one[11])
        add_data.append(one[14])
        add_data.append(one[15])
        add_data.append(one[17])
        add_data.append(one[18])
        add_data.append(one[19])
        add_data.append(one[20])
        add_data.append(one[21])
        add_data.append(one[22])
        add_data.append(one[23])
        add_data.append(one[25])
        add_data.append(one[32])
        add_data.append(one[35])
        add_data.append(one[38])
        add_data.append(one[39])
        add_data.append(one[100])
        add_data.append(one[102])
        add_data.append(one[103])
        add_data.append(one[104])
        add_data.append(one[107])
        add_data.append(one[108])
        add_data.append(one[109])
        add_data.append(one[110])
        add_data.append(one[111])
        add_data.append(one[112])
        add_data.append(one[113])
        add_data.append(one[114])
        add_data.append(one[115])
        add_data.append(one[116])
        add_data.append(one[117])
        add_data.append(one[118])
        add_data.append(one[119])
        add_data.append(one[120])
        add_data.append(one[121])
        add_data.append(one[122])
        add_data.append(one[123])
        add_data.append(one[124])
        add_data.append(one[125])
        add_data.append(one[126])
        add_data.append(one[127])
        add_data.append(one[128])
        add_data.append(one[129])
        add_data.append(one[130])
        add_data.append(one[131])
        add_data.append(one[132])
        add_data.append(one[133])
        add_data.append(one[134])
        add_data.append(one[135])
        add_data.append(one[136])
        add_data.append(one[137])
        add_data.append(one[138])
        add_data.append(one[139])
        add_data.append(one[140])
        add_data.append(one[141])
        add_data.append(one[142])
        add_data.append(one[143])

        add_data.append(one[44])
        add_data.append(one[45])
        add_data.append(one[46])
        add_data.append(one[47])
        add_data.append(one[48])
        add_data.append(one[49])
        add_data.append(one[50])
        add_data.append(one[51])
        add_data.append(one[52])
        add_data.append(one[53])
        add_data.append(one[55])

        add_data.append(one[69])
        add_data.append(one[70])
        add_data.append(one[71])
        add_data.append(one[72])
        add_data.append(one[73])
        add_data.append(one[74])
        add_data.append(one[75])
        add_data.append(one[76])
        add_data.append(one[77])
        add_data.append(one[78])
        add_data.append(one[79])
        add_data.append(one[80])
        add_data.append(one[81])
        add_data.append(one[82])
        add_data.append(one[83])
        add_data.append(one[84])
        add_data.append(one[85])
        add_data.append(one[86])
        add_data.append(one[87])
        add_data.append(one[88])
        add_data.append(one[89])
        add_data.append(one[90])
        add_data.append(one[91])
        add_data.append(one[92])
        add_data.append(one[93])
        add_data.append(one[94])
        add_data.append(one[95])
        add_data.append(one[96])
        add_data.append(one[97])
        add_data.append(one[98])

        add_data.append(one[160])
        add_data.append(one[161])
        add_data.append(one[165])
        new_data.append(add_data)
    return new_data

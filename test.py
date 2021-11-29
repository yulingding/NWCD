from django.shortcuts import render
import xlrd
from .models import Site,Pds_inlet,Pds_outlet,Swgr_inlet,Swgr_outlet,Swbd_outlet,Ups,Udp,Rpp
from .models import Rack,Rack_config
## power config dashboard
def power_config_dashboard(request):
    username = request.user
    power_list = Rack_config.objects.all()[0:600]
    return render(request,'nwcd_eam/power_dashboard.html',locals())

## power search function
def power_config_search(request):
    return render()
    
## power add function
def power_config_add(request):
    return render()

## power update function
def power_config_update(request):
    return render()

## power delete function
def power_config_delete(request):
    return render()

## power open number add function
def power_config_add_open(request):
    return 'ok'



def excel_migrate():
    workbook = xlrd.open_workbook('/Users/mac/Desktop/worksapce/nwcd_master/nwcd_eam/zhy52.xlsx')
    get_sheet_name0 = workbook.sheet_names()[0]
    sheet0 = workbook.sheet_by_name(get_sheet_name0)
    norws0 = sheet0.nrows

    # init var
    last_site = 'ZHY52'
    last_pdsinlet = ''
    last_pdsoutlet = ''
    last_swgrinlet = ''
    last_swgroutlet = ''
    last_swbdoutlet = ''
    last_uspnumber = ''
    last_udpnumber = ''
    last_rppnumber = ''
    last_racknumber = ''
    for i in range(1, 6187):

        rowvaule = sheet0.row_values(i)

        site = str(rowvaule[0])
        supply_type = str(rowvaule[1])
        rack_type = str(rowvaule[2])
        racknumber = str(rowvaule[3]).replace('.0','')
        plugnumber = str(rowvaule[4])
        opennumber = str(rowvaule[5])
        rppnumber = str(rowvaule[6])
        podnumber = str(rowvaule[7])
        udpnumber = str(rowvaule[8])
        uspnumber = str(rowvaule[9])
        ccunumber = str(rowvaule[10])
        swbdoutlet = str(rowvaule[11])
        swgroutlet = str(rowvaule[12])
        swgrinlet = str(rowvaule[13])
        pdsoutlet = str(rowvaule[14])
        pdsinlet = str(rowvaule[15])
        atsno = str(rowvaule[16])
        atssn = str(rowvaule[17])
        rpduno = str(rowvaule[18])
        rpdutype = str(rowvaule[19])

        #add pds
    
        if pdsinlet != last_pdsinlet:
            new_pdsinlet =  Pds_inlet(site_id = 1, pds_inlet=pdsinlet)
            new_pdsinlet.save()

        last_pdsinlet = pdsinlet
        '''
        if pdsoutlet != last_pdsoutlet:
            pdsinlet_id = Pds_inlet.objects.get(pds_inlet=pdsinlet).id
            new_pdsoutlet = Pds_outlet(pds_inlet_id = pdsinlet_id,pds_outlet = pdsoutlet)
            new_pdsoutlet.save()

        last_pdsoutlet = pdsoutlet

        if swgrinlet != last_swgrinlet:
            pdsoutlet_id = Pds_outlet.objects.get(pds_outlet = pdsoutlet).id
            new_swgrinlet = Swgr_inlet(pds_outlet_id = pdsoutlet_id,swgt_inlet = swgrinlet)
            new_swgrinlet.save()

        last_swgrinlet = swgrinlet
        if swgroutlet != last_swgroutlet:
            swgrinlet_id = Swgr_inlet.objects.get(swgt_inlet = swgrinlet).id
            new_swgroutlet =  Swgr_outlet(swgr_inlet_id = swgrinlet_id,swgr_outlet = swgroutlet)
            new_swgroutlet.save()
        last_swgroutlet = swgroutlet

        if swbdoutlet != last_swbdoutlet:
            swgroutlet_id = Swgr_outlet.objects.get(swgr_outlet = swgroutlet).id
            new_swbdoutlet = Swbd_outlet(swgr_outlet_id = swgroutlet_id,swbd_outlet = swbdoutlet)
            new_swbdoutlet.save()
        last_swbdoutlet = swbdoutlet

        
        if uspnumber != last_uspnumber:
            swbdoutlet_id = Swbd_outlet.objects.get(swbd_outlet = swbdoutlet).id
            new_uspnumber = Ups(ups_number=uspnumber,swbd_outlet_id=swbdoutlet_id)
            new_uspnumber.save()
        last_uspnumber = uspnumber
        
        if udpnumber != last_udpnumber:
            ups_id = Ups.objects.get(ups_number = uspnumber).id
            new_udp = Udp(ups_id=ups_id,udp_number=udpnumber)
            new_udp.save()
        last_udpnumber = udpnumber
        
        if rppnumber != last_rppnumber:
            udp_id = Udp.objects.get(udp_number = udpnumber).id
            new_rpp = Rpp(udp_id=udp_id,rpp_number = rppnumber)
            new_rpp.save()
        last_rppnumber = rppnumber
        
        if racknumber != last_racknumber:
            rack = Rack(rack_number = racknumber,pod=podnumber,
                        rack_type=rack_type,supply_type=supply_type,
                        rpdu_type = rpdutype,ccu_number= ccunumber
                        )
            rack.save()
        last_racknumber = racknumber
        
        site_id = 1
        rack_id = Rack.objects.filter(rack_number = racknumber,rack_type=rack_type,supply_type=supply_type).first().id        
        rpp_id = Rpp.objects.get(rpp_number = rppnumber).id
        rack_config = Rack_config(
                    rack_id= rack_id,rpp_id=rpp_id,site_id=site_id,
                    open_number = opennumber,
                    plug_number = plugnumber,
                    ats_number = atsno,
                    ats_sn = atssn,
                    rpdu_number=rppnumber
                    )
        rack_config.save()
        '''



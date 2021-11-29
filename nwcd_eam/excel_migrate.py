import xlrd

def excel_migrate():
    workbook = xlrd.open_workbook('C:/workspace/nwcd_master/nwcd_eam/zhy52.xlsx')
    get_sheet_name0 = workbook.sheet_names()[0]
    sheet0 = workbook.sheet_by_name(get_sheet_name0)
    norws0 = sheet0.nrows

    for i in range(1, norws0):
        rowvaule = sheet0.row_values(i)

        site = str(rowvaule[0])
        supply_type = str(rowvaule[1])
        rack_type = str(rowvaule[2])
        racknumber = str(int(rowvaule[3]))
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
        
        print(locals())

excel_migrate()
        
from django.contrib import admin
from django.contrib.admin.helpers import InlineFieldset
from django.db.models import fields

# Register your models here.
from .models import Site,Pds_inlet,Pds_outlet,Swgr_inlet,Swgr_outlet,Swbd_outlet,Ups,Udp,Rpp
from .models import Rack,Rack_config,Equipment_config



class Pds_inletAdmin(admin.ModelAdmin):
    list_display = ('pds_inlet','site')   
    list_filter = ('pds_inlet','site')
    list_per_page = 50
class Pds_outletAdmin(admin.ModelAdmin):
    list_display = ('pds_outlet','pds_inlet')
    list_filter = ('pds_outlet','pds_inlet')
    list_per_page = 50
class Swgr_inletAdmin(admin.ModelAdmin):
    list_display = ('swgt_inlet','pds_outlet')
    list_filter = ('swgt_inlet','pds_outlet')
    list_per_page = 50
class Swgr_outletAdmin(admin.ModelAdmin):
    list_display = ('swgr_outlet','swgr_inlet')
    list_filter = ('swgr_outlet','swgr_inlet')
    list_per_page = 50

class Swbd_outletAdmin(admin.ModelAdmin):
    list_display = ('swbd_outlet','swgr_outlet')
    list_filter  = ('swbd_outlet','swgr_outlet')
    list_per_page = 50

class UpsAdmin(admin.ModelAdmin):
    list_display = ('ups_number','swbd_outlet')
    list_filter  = ('ups_number','swbd_outlet')
    list_per_page = 50

class UdpAdmin(admin.ModelAdmin):
    list_display = ('udp_number','ups')
    list_filter =  ('udp_number','ups')
    list_per_page = 50

class RppAdmin(admin.ModelAdmin):
    list_display = ('rpp_number','udp')
    list_filter =  ('rpp_number','udp')
    list_per_page = 50

class RackAdmin(admin.ModelAdmin):
    list_display = ('rack_number','pod','rack_type','supply_type','rpdu_type','ccu_number')
    list_filter = ('rack_number','pod','rack_type','supply_type','rpdu_type','ccu_number')
    list_per_page = 50



class Equipment_configAdmin(admin.ModelAdmin):
    list_display = ('update_DateTime','configuration_Item_Name','configuration_Item_Description',
                    'configuration_Item_Value','previouse_item_value',
                    'modificaiton_Methods','configuration_Item_Value_Range',
                    'configuration_Item_Value_Type','condition_For_Validity',
                    'configuration_Item_Level','software_Name','device_Name',
                    'device_Description','subsystem', 'system','facility','site','come_From','more_Remark')
    list_per_page = 50

########################################
########################################
admin.site.site_header = 'NWCD_DC_ADMIN'
admin.site.register(Site)
admin.site.register(Pds_inlet,Pds_inletAdmin)
admin.site.register(Pds_outlet,Pds_outletAdmin)
admin.site.register(Swgr_inlet,Swgr_inletAdmin)
admin.site.register(Swgr_outlet,Swgr_outletAdmin)
admin.site.register(Swbd_outlet,Swbd_outletAdmin)
admin.site.register(Ups,UpsAdmin)
admin.site.register(Udp,UdpAdmin)
admin.site.register(Rpp,RppAdmin)
admin.site.register(Rack,RackAdmin)
admin.site.register(Equipment_config,Equipment_configAdmin)
from django.contrib import admin

from .models import Limak_Sirket,Firma,Sozlesme


class SozlesmelerAdmin(admin.ModelAdmin):
      list_display=('id','created_date','sözlesme_no')
      list_display_links =('id','created_date','sözlesme_no')
      search_fields =('sözlesme_no',)
      

      
class FirmaAdmin(admin.ModelAdmin):

      list_display=('id','firma_kodu','firma')
      list_display_links =('id','firma_kodu','firma')

class LimakAdmin(admin.ModelAdmin):
      list_display =('id','limak_kodu', 'limak_sirketi')
      list_display_links =('id','limak_kodu', 'limak_sirketi')


admin.site.register(Limak_Sirket,LimakAdmin)
admin.site.register(Firma,FirmaAdmin)
admin.site.register(Sozlesme,SozlesmelerAdmin)

    
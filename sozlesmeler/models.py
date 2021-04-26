from django.db import models

class Limak_Sirket(models.Model):
      kod=(
          ('Limak Holding','Limak Holding'),
          ('Limak İnşaat','Limak inşaat'),
          ('Limak Yatırım','Limak Yatırım'),
      )
      kod1=(
          ('000','000'),
          ('001','001'),
          ('002','002'),
      )
      limak_kodu= models.CharField(max_length=12,choices=kod1, verbose_name= 'Limak Kodu')
      limak_sirketi = models.CharField(max_length=35, choices=kod, verbose_name= 'Limak Şirketleri')

      def __str__(self):
          return self.limak_kodu 
 
          

class Firma(models.Model):

      kod2=(
          ('Otokoç','Otokoç'),
          ('Ayder','Ayder'),
          ('Tan Oto','Tan Oto'),
      )
      kod3=(
          ('001','001'),
          ('002','002'),
          ('003','003'),
      )
      firma_kodu= models.CharField(max_length=12,choices=kod3, verbose_name= 'Firma Kodu')
      firma= models.CharField(max_length=45, choices=kod2, verbose_name= 'Firma Adı')

      def __str__(self):
          return self.firma_kodu
    

class Sozlesme(models.Model):

      sözlesme_no= models.CharField(max_length=3,verbose_name='Sözlesme Numarası')
      limak = models.ForeignKey(Limak_Sirket, on_delete=models.CASCADE)
      firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
      created_date= models.DateTimeField(auto_now_add= True, verbose_name='Eklenme Tarihi')
      image= models.FileField(blank= True, null= True, verbose_name='Sözleşme dosyası')

      

     
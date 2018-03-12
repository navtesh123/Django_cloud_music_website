from rest_framework import serializers

 class StockSerializer(serializers.ModelSerializer):
     class Meta:
         model=Stock
         fields=('ticker','volume')
         #fields='__all__'  (for all fields)

from django.contrib import admin
from .models import *
from django.db.models import Q
from django.utils.html import format_html
from django.urls import reverse

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen menulary poz" 
admin.site.register(Menu,MenuAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('menu','name','date')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen kategoriyalary poz"
admin.site.register(Category,CategoryAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('bannerImage','name','link','date')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen bannerleri poz"
    
    def bannerImage(slef,obj):
        return format_html('<img src="{0}" width="200px" height="100px">'.format(obj.image.url))
admin.site.register(Banner,BannerAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','brandImage',)
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen brendleri poz"
        
    def brandImage(slef,obj):
        return format_html('<img src="{0}" width="80px" height="80px" style="border-radius:50%;border:2px solid #000;">'.format(obj.image.url))
admin.site.register(Brand,BrandAdmin)

class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Baha aralygy'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return [
            ('0-100', '0 - 100'),
            ('100-500', '100 - 500'),
            ('500-1000', '500 - 1000'),
            ('1000-5000', '1000 - 5000'),
            ('5000-10000', '5000-10000'),
            ('10000-20000', '10000-20000'),
        ]
    
    def queryset(self, request, queryset):
        if self.value():
            min_price, max_price = map(int, self.value().split('-'))

            if max_price == 100000:
                return queryset.filter(price__gte=min_price)
            elif max_price == 100000:
                return queryset.filter(price__gte=min_price, price__gt=5000)
            else:
                return queryset.filter(Q(price__gte=min_price) & Q(price__lte=max_price))
        return queryset

class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('productName',)
    list_display = ('id','productImage','productName','brand','baha','konebaha','status','date')
    search_fields = ('productCode','productName','price','brand__name')
    list_filter = (PriceRangeFilter,)
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen harytlary poz"

    def baha(self, obj):
        return f'{obj.price} TMT'
    baha.short_description = 'Baha'
    def konebaha(self, obj):
        return f'{obj.oldPrice} TMT'
    konebaha.short_description = 'Kone Baha'

    def get_image_count(self, obj):
        return obj.images.count()
    
    def productImage(slef,obj):
        return format_html('<img src="{0}" width="80px" height="80px" style="object-fit:contain; border-radius:5px;border:2px solid #000;">'.format(obj.image.url))
admin.site.register(Product,ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    search_fields = ('product__productName',)
    list_display = ('product','images')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen haryt suratlaryny poz"
admin.site.register(ProductImages,ProductImageAdmin)

# class ColorAdmin(admin.ModelAdmin):
#     list_display = ('colorCodeRender','colorName')
# admin.site.register(Color)

# class ProductColorAdmin(admin.ModelAdmin):
#     search_fields = ('product__productName',)
#     list_display = ('product','colorInfo','colorImage')
# admin.site.register(ProductColor,ProductColorAdmin)

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('user__username','product__productName','product__productCode','comment',)
    list_display = ('user','product','comment','rate','created_at')
    list_filter = ('rate',)
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen teswirleri poz"
admin.site.register(Review,ReviewAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user','product_link','quantity','add_time')
    actions = ['delete_selected']

    def product_link(self, obj):
        product_url = reverse('product', args=[obj.product.pk, obj.product.productName])
        return format_html('<a href="{}">{}</a>', product_url, obj.product)
    product_link.short_description = 'Haryt'

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen sebetleri poz"
admin.site.register(Cart,CartAdmin)

class WishlistAdmin(admin.ModelAdmin):
    search_fields = ('user__username','product__productName','product__productCode')
    list_display = ('user','product')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen halananlary poz"
admin.site.register(Wishlist,WishlistAdmin)

admin.site.register(City)
admin.site.register(Etrap)

class AdressAdmin(admin.ModelAdmin):
    list_display = ('user','name','last_name','city','city_etrap','time')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen salgylary poz"
admin.site.register(Adress,AdressAdmin)

class OrderAdmin(admin.ModelAdmin):
    search_fields = ('user__username','product')
    list_display = ('user','productCode','product','productImg','quantity','price','adress','total','payment_choices','status','date')
    list_filter = ('payment_choices','status')
    actions = ['delete_selected']

    # def product_link(self, obj):
    #     product_url = reverse('product', args=[obj.product.pk, obj.product.productName])
    #     return format_html('<a href="{}">{}</a>', product_url, obj.product)
    # product_link.short_description = 'Haryt'

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen sargytlary poz"

    def get_image_count(self, obj):
        return obj.images.count()
    
    def productImg(slef,obj):
        return format_html('<img src="{0}" width="80px" height="80px" style="object-fit:contain; border-radius:5px;border:2px solid #000;">'.format(obj.productImage))
admin.site.register(Order,OrderAdmin)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('description','logo')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen Hakdany poz"

    def get_image_count(self, obj):
        return obj.images.count()
    
    def logo(self,obj):
        return format_html('<img src="{0}" width="80px" height="80px" style="object-fit:contain; border-radius:5px;border:2px solid #000;">'.format(obj.image.url))
admin.site.register(AboutUs,AboutUsAdmin)

class HelpAdmin(admin.ModelAdmin):
    list_display = ('question','answer')

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen Soraglary poz"

admin.site.register(Help,HelpAdmin)

class ExchangeConditionAdmin(admin.ModelAdmin):
    list_display = ("condition",)
    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen Calşyp bermek şertlerini poz"

admin.site.register(ExchangeCondition,ExchangeConditionAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','lastName','message')
    search_fields = ('message','name','lastName')
    def delete_selected(self, request, queryset):
        for item in queryset:
            item.delete_with_related()
    delete_selected.short_description = "Seçilen Hatlary poz"

admin.site.register(Contact,ContactAdmin)
from django.core.management.base import BaseCommand
from products.models import Category, Product, Review
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds production-grade initial products, categories, and reviews'

    def handle(self, *args, **options):
        self.stdout.write("Seeding real production-like e-commerce data...")

        # Clear existing products, categories, reviews for clean state
        Review.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create Demo Admin/Staff User and Customer User
        admin_user, _ = User.objects.get_or_create(
            phone_number='+998901234567',
            defaults={'is_staff': True, 'is_superuser': True}
        )
        admin_user.set_password('admin123')
        admin_user.save()

        customer_user, _ = User.objects.get_or_create(
            phone_number='+998919876543',
            defaults={'is_staff': False}
        )
        customer_user.set_password('user123')
        customer_user.save()

        # Define Categories
        categories_data = [
            {'name': 'Smartfonlar va Gadjetlar'},
            {'name': 'Noutbuklar va Kompyuterlar'},
            {'name': 'Audio va Quloqchinlar'},
            {'name': 'Aqlli Soatlar'},
            {'name': 'Kitoblar va Ta\'lim'},
            {'name': 'Kiyim va Aksessuarlar'},
            {'name': 'Uy va Maishiy Texnika'}
        ]

        cat_map = {}
        for c_data in categories_data:
            cat_obj = Category.objects.create(name=c_data['name'])
            cat_map[c_data['name']] = cat_obj

        # Define Real Products
        products_data = [
            # Smartfonlar va Gadjetlar
            {
                'name': 'iPhone 15 Pro Max 256GB Titanium',
                'description': 'A17 Pro super chip, Titanium yengil va mustahkam korpus, 48MP asosiy kamera hamda Action Button.',
                'price': 1299.00,
                'category': cat_map['Smartfonlar va Gadjetlar'],
                'stock': 15,
                'reviews': [
                    {'user': admin_user, 'rating': 5, 'content': 'Kamera va displey sifati shunchaki dahshat! Batareya 2 kunga etadi.'},
                    {'user': customer_user, 'rating': 5, 'content': 'Dizayni juda yengil va qo\'lda juda qulay o\'tiradi.'}
                ]
            },
            {
                'name': 'Samsung Galaxy S24 Ultra 512GB',
                'description': 'Galaxy AI sun\'iy intellekt xususiyatlari, Titanium ramka, 200MP kamera va o\'rnatilgan S Pen qalami.',
                'price': 1199.00,
                'category': cat_map['Smartfonlar va Gadjetlar'],
                'stock': 20,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'AI foto tahrirlash va matn tarjima funksiyalari super!'}
                ]
            },
            {
                'name': 'Google Pixel 8 Pro 128GB',
                'description': 'Tensor G3 chipi, eng ilg\'or Android kamerasi, Magic Eraser va 7 yillik rasmiy yangilanishlar.',
                'price': 899.00,
                'category': cat_map['Smartfonlar va Gadjetlar'],
                'stock': 8,
                'reviews': [
                    {'user': admin_user, 'rating': 4, 'content': 'Toza Android va zo\'r AI kameralar.'}
                ]
            },

            # Noutbuklar va Kompyuterlar
            {
                'name': 'MacBook Pro 16" M3 Max 36GB/1TB',
                'description': 'Apple M3 Max chipi, 36GB birlashtirilgan xotira, Liquid Retina XDR displey va 22 soatgacha batareya amali.',
                'price': 3499.00,
                'category': cat_map['Noutbuklar va Kompyuterlar'],
                'stock': 10,
                'reviews': [
                    {'user': admin_user, 'rating': 5, 'content': 'Dasturlash va 4K video montaj uchun eng kuchli noutbuk!'}
                ]
            },
            {
                'name': 'MacBook Air 15" M2 8GB/512GB',
                'description': 'Ultra-yupqa va yengil dizayn, ovozsiz passiv sovutish hamda kun bo\'yi yetuvchi batareya.',
                'price': 1299.00,
                'category': cat_map['Noutbuklar va Kompyuterlar'],
                'stock': 25,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'O\'qish va kunda kunda ishlatish uchun ideal noutbuk.'}
                ]
            },
            {
                'name': 'ASUS ROG Zephyrus G16 OLED Gaming',
                'description': 'Intel Core Ultra 9, RTX 4080 12GB, 240Hz ROG Nebula OLED displey va premium alyuminiy korpus.',
                'price': 2499.00,
                'category': cat_map['Noutbuklar va Kompyuterlar'],
                'stock': 6,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'O\'yinlarda barcha grafikalar Ultra rejimida ishlaydi!'}
                ]
            },

            # Audio va Quloqchinlar
            {
                'name': 'Sony WH-1000XM5 Wireless Headphones',
                'description': 'Sanoatdagi eng ilg\'or shovqinni so\'ndirish (ANC), 30 soat batareya va kristaldek toza mikrafonlar.',
                'price': 399.00,
                'category': cat_map['Audio va Quloqchinlar'],
                'stock': 30,
                'reviews': [
                    {'user': admin_user, 'rating': 5, 'content': 'Samolyot va shovqinli joylarda shovqin so\'ndirish ajoyib.'}
                ]
            },
            {
                'name': 'AirPods Pro (2nd Gen) USB-C',
                'description': 'Active Noise Cancellation, Adaptive Audio, Personalised Spatial Audio va MagSafe (USB-C) g\'ilof.',
                'price': 249.00,
                'category': cat_map['Audio va Quloqchinlar'],
                'stock': 45,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'Apple ekotizimida eng qulay va kompakt quloqchin.'}
                ]
            },
            {
                'name': 'Marshall Stanmore III Bluetooth Spiker',
                'description': 'Afsonaviy rok dizayni, chuqur bas va keng dinamik diapozonli uydagi simsiz kolonka.',
                'price': 379.00,
                'category': cat_map['Audio va Quloqchinlar'],
                'stock': 12,
                'reviews': [
                    {'user': admin_user, 'rating': 5, 'content': 'Ovoz kuchi va vintaj dizayniga gap yo\'q!'}
                ]
            },

            # Aqlli Soatlar
            {
                'name': 'Apple Watch Ultra 2 GPS + Cellular',
                'description': 'Titanium 49mm korpus, 3000 nits super yorqin ekran, Double Tap jesti hamda 36 soat batareya.',
                'price': 799.00,
                'category': cat_map['Aqlli Soatlar'],
                'stock': 14,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'Sportchilar va ekstremal sayohatlar uchun zo\'r soat.'}
                ]
            },
            {
                'name': 'Samsung Galaxy Watch6 Classic 47mm',
                'description': 'Aylanuvchi mexanik bezel, uyqu va yurak urishini monitoring qilish, Wear OS operatsion tizimi.',
                'price': 349.00,
                'category': cat_map['Aqlli Soatlar'],
                'stock': 22,
                'reviews': [
                    {'user': admin_user, 'rating': 4, 'content': 'Klassik va zamonaviy dizayn uyg\'unligi.'}
                ]
            },

            # Kitoblar va Ta'lim
            {
                'name': 'Atomic Habits (Atom Odatlar) - James Clear',
                'description': 'Kichik 1% o\'zgarishlar orqali hayotni tubdan o\'zgartirish va yaxshi odatlarni shakllantirish bo\'yicha bestseller.',
                'price': 18.00,
                'category': cat_map['Kitoblar va Ta\'lim'],
                'stock': 100,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'Har bir inson o\'qib chiqishi shart bo\'lgan ajoyib kitob!'}
                ]
            },
            {
                'name': 'Clean Code (Toza Kod) - Robert C. Martin',
                'description': 'Dasturchilar va arxitektorlar uchun tushunarli, qayta ishlatiladigan va mukammal kod yozish qo\'llanmasi.',
                'price': 35.00,
                'category': cat_map['Kitoblar va Ta\'lim'],
                'stock': 50,
                'reviews': [
                    {'user': admin_user, 'rating': 5, 'content': 'Dasturlash sohasidagi fundamental va muhim kitoblardan biri.'}
                ]
            },
            {
                'name': 'Deep Work (Chukur Ishlash) - Cal Newport',
                'description': 'Chalg\'ituvchi dunyoda diqqatni jamlash va yuqori samaradorlikka erishish sirlari.',
                'price': 22.00,
                'category': cat_map['Kitoblar va Ta\'lim'],
                'stock': 65,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'Diqqat va samaradorlikni oshirish uchun ajoyib qo\'llanma.'}
                ]
            },

            # Kiyim va Aksessuarlar
            {
                'name': 'Nike Air Jordan 1 Retro High OG',
                'description': 'Afsonaviy basketbol krossovkasi, premium tabiiy charm va mashhur klassik ranglar uyg\'unligi.',
                'price': 180.00,
                'category': cat_map['Kiyim va Aksessuarlar'],
                'stock': 18,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'Dizayni va qulayligi o\'ta yuqori darajada.'}
                ]
            },
            {
                'name': 'Ray-Ban Wayfarer Classic Quyosh Ko\'zoynagi',
                'description': '1956 yildan beri mashhur bo\'lgan klassik dizayn, 100% UV himoyali va polarlangan linzalar.',
                'price': 165.00,
                'category': cat_map['Kiyim va Aksessuarlar'],
                'stock': 25,
                'reviews': [
                    {'user': admin_user, 'rating': 5, 'content': 'Har qanday kiyim bilan juda chiroyli ko\'rinadi.'}
                ]
            },

            # Uy va Maishiy Texnika
            {
                'name': 'Dyson V15 Detect Cordless Vacuum',
                'description': 'Lazerli chang aniqlash texnologiyasi, PIEZO sensori va o\'ta kuchli so\'rish quvvati.',
                'price': 749.00,
                'category': cat_map['Uy va Maishiy Texnika'],
                'stock': 9,
                'reviews': [
                    {'user': customer_user, 'rating': 5, 'content': 'Uy tozalash endi juda tez va oson bo\'lib qoldi!'}
                ]
            },
            {
                'name': 'DeLonghi Magnifica S Kofe Mashinasi',
                'description': 'Yangi kofe donalaridan espresso va kapuchino tayyorlovchi avtomatik kofe mashinasi.',
                'price': 529.00,
                'category': cat_map['Uy va Maishiy Texnika'],
                'stock': 11,
                'reviews': [
                    {'user': admin_user, 'rating': 5, 'content': 'Har kuni ertalab kafedagidek mazali kofe!'}
                ]
            }
        ]

        for p in products_data:
            reviews_data = p.pop('reviews', [])
            product_obj = Product.objects.create(**p)

            for r in reviews_data:
                Review.objects.create(
                    product=product_obj,
                    user=r['user'],
                    rating=r['rating'],
                    content=r['content']
                )

        self.stdout.write(self.style.SUCCESS(
            f"Successfully seeded data: Categories: {Category.objects.count()}, Products: {Product.objects.count()}, Reviews: {Review.objects.count()}"
        ))

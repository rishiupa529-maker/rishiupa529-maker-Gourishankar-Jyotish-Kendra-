from django.db import models

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('kundli', 'कुंडली विश्लेषण (Kundli Analysis)'),
        ('vastu', 'वास्तु परामर्श (Vastu Consultation)'),
        ('matchmaking', 'गुण मिलान (Matchmaking)'),
        ('puja', 'पूजा एवं अनुष्ठान (Puja & Anushthan)'),
        ('gemstone', 'रत्न परामर्श (Gemstone Advice)'),
        ('other', 'अन्य (Other)'),
    ]

    full_name = models.CharField(max_length=100, verbose_name="पूरा नाम")
    phone = models.CharField(max_length=15, verbose_name="फ़ोन नंबर")
    email = models.EmailField(blank=True, null=True, verbose_name="ईमेल")
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, verbose_name="सेवा")
    preferred_date = models.DateField(verbose_name="तारीख")
    preferred_time = models.TimeField(verbose_name="समय")
    birth_details = models.TextField(blank=True, null=True, verbose_name="जन्म विवरण")
    message = models.TextField(blank=True, null=True, verbose_name="अतिरिक्त संदेश")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"
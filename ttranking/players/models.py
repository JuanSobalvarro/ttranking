# ttranking/players/models.py
from django.contrib.auth.models import User
from django.db import models
from django.core.files.base import ContentFile
from datetime import date
from PIL import Image
import io
import os
from uuid import uuid4
import math


# Define a tuple of tuples with country code and country name
COUNTRY_CHOICES = [
    ('AF', 'Afganistán'),
    ('AL', 'Albania'),
    ('DZ', 'Argelia'),
    ('AO', 'Angola'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaiyán'),
    ('BS', 'Bahamas'),
    ('BH', 'Baréin'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Bielorrusia'),
    ('BE', 'Bélgica'),
    ('BZ', 'Belice'),
    ('BJ', 'Benín'),
    ('BT', 'Bután'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia y Herzegovina'),
    ('BW', 'Botswana'),
    ('BR', 'Brasil'),
    ('BN', 'Brunéi'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Camboya'),
    ('CM', 'Camerún'),
    ('CA', 'Canadá'),
    ('CV', 'Cabo Verde'),
    ('CF', 'República Centroafricana'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('KM', 'Comoras'),
    ('CG', 'Congo'),
    ('CD', 'República Democrática del Congo'),
    ('CR', 'Costa Rica'),
    ('CI', 'Costa de Marfil'),
    ('HR', 'Croacia'),
    ('CU', 'Cuba'),
    ('CY', 'Chipre'),
    ('CZ', 'República Checa'),
    ('DK', 'Dinamarca'),
    ('DJ', 'Yibuti'),
    ('DM', 'Dominica'),
    ('DO', 'República Dominicana'),
    ('EC', 'Ecuador'),
    ('EG', 'Egipto'),
    ('SV', 'El Salvador'),
    ('GQ', 'Guinea Ecuatorial'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Etiopía'),
    ('FJ', 'Fiyi'),
    ('FI', 'Finlandia'),
    ('FR', 'Francia'),
    ('GA', 'Gabón'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Alemania'),
    ('GH', 'Ghana'),
    ('GR', 'Grecia'),
    ('GD', 'Granada'),
    ('GT', 'Guatemala'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-Bisáu'),
    ('GY', 'Guyana'),
    ('HT', 'Haití'),
    ('HN', 'Honduras'),
    ('HU', 'Hungría'),
    ('IS', 'Islandia'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Irán'),
    ('IQ', 'Irak'),
    ('IE', 'Irlanda'),
    ('IL', 'Israel'),
    ('IT', 'Italia'),
    ('JM', 'Jamaica'),
    ('JP', 'Japón'),
    ('JO', 'Jordania'),
    ('KZ', 'Kazajistán'),
    ('KE', 'Kenia'),
    ('KI', 'Kiribati'),
    ('KP', 'Corea del Norte'),
    ('KR', 'Corea del Sur'),
    ('KW', 'Kuwait'),
    ('KG', 'Kirguistán'),
    ('LA', 'Laos'),
    ('LV', 'Letonia'),
    ('LB', 'Líbano'),
    ('LS', 'Lesoto'),
    ('LR', 'Liberia'),
    ('LY', 'Libia'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lituania'),
    ('LU', 'Luxemburgo'),
    ('MK', 'Macedonia del Norte'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malasia'),
    ('MV', 'Maldivas'),
    ('ML', 'Malí'),
    ('MT', 'Malta'),
    ('MH', 'Islas Marshall'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauricio'),
    ('MX', 'México'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldavia'),
    ('MC', 'Mónaco'),
    ('MN', 'Mongolia'),
    ('ME', 'Montenegro'),
    ('MA', 'Marruecos'),
    ('MZ', 'Mozambique'),
    ('MM', 'Birmania'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Países Bajos'),
    ('NZ', 'Nueva Zelanda'),
    ('NI', 'Nicaragua'),
    ('NE', 'Níger'),
    ('NG', 'Nigeria'),
    ('NO', 'Noruega'),
    ('OM', 'Omán'),
    ('PK', 'Pakistán'),
    ('PW', 'Palaú'),
    ('PS', 'Territorio Palestino Ocupado'),
    ('PA', 'Panamá'),
    ('PG', 'Papúa Nueva Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Perú'),
    ('PH', 'Filipinas'),
    ('PL', 'Polonia'),
    ('PT', 'Portugal'),
    ('QA', 'Catar'),
    ('RO', 'Rumania'),
    ('RU', 'Federación Rusa'),
    ('RW', 'Ruanda'),
    ('KN', 'San Cristóbal y Nieves'),
    ('LC', 'Santa Lucía'),
    ('VC', 'San Vicente y las Granadinas'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Santo Tomé y Príncipe'),
    ('SA', 'Arabia Saudita'),
    ('SN', 'Senegal'),
    ('RS', 'Serbia'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leona'),
    ('SG', 'Singapur'),
    ('SK', 'Eslovaquia'),
    ('SI', 'Eslovenia'),
    ('SB', 'Islas Salomón'),
    ('SO', 'Somalia'),
    ('ZA', 'Sudáfrica'),
    ('SS', 'Sudán del Sur'),
    ('ES', 'España'),
    ('LK', 'Sri Lanka'),
    ('SD', 'Sudán'),
    ('SR', 'Surinam'),
    ('SZ', 'Suazilandia'),
    ('SE', 'Suecia'),
    ('CH', 'Suiza'),
    ('SY', 'Siria'),
    ('TW', 'Taiwán'),
    ('TJ', 'Tayikistán'),
    ('TZ', 'Tanzania'),
    ('TH', 'Tailandia'),
    ('TL', 'Timor-Leste'),
    ('TG', 'Togo'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad y Tobago'),
    ('TN', 'Túnez'),
    ('TR', 'Turquía'),
    ('TM', 'Turkmenistán'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ucrania'),
    ('AE', 'Emiratos Árabes Unidos'),
    ('GB', 'Reino Unido'),
    ('US', 'Estados Unidos'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistán'),
    ('VU', 'Vanuatu'),
    ('VE', 'Venezuela'),
    ('VN', 'Vietnam'),
    ('YE', 'Yemen'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabue'),
]


GENDER_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino')
]

DESIRED_SIZE = (600, 600)


def get_image_upload_path(instance, filename):
    # Generate a unique filename
    ext = filename.split('.')[-1]
    new_filename = f'{uuid4().hex}.{ext}'
    return os.path.join('player_photos/', new_filename)


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=False, blank=True, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    ranking = models.IntegerField(default=0, blank=True)
    matches_played = models.IntegerField(default=0, blank=True)
    photo = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def age(self) -> int:
        if self.date_of_birth is None:
            return None
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (today.year, today.year))

    @property
    def victories(self):
        """
        Returns the number of victories this player has based on his ranking.
        :return:
        """
        return int(self.ranking / 2)

    @property
    def winrate(self) -> float:
        """
        Returns the winrate of the player based on his ranking.
        :return:
        """
        if self.matches_played == 0:
            return 0
        return math.trunc(self.ranking / self.matches_played * 50)

    def add_points(self, points):
        self.ranking += points
        self.save()

    def remove_points(self, points):
        self.ranking -= points
        self.save()

    def save(self, *args, **kwargs):
        if self.pk:
            # Get the previous photo from the database
            old_player = Player.objects.get(pk=self.pk)
            old_photo = old_player.photo

            if old_photo and old_photo != self.photo:
                if os.path.isfile(old_photo.path):
                    os.remove(old_photo.path)

        if self.photo:
            # Open the image file
            image = Image.open(self.photo)

            # Resize and crop the image
            image = self.resize_and_crop(image, DESIRED_SIZE)

            # Save the image to a BytesIO object
            buffer = io.BytesIO()
            image.save(buffer, format='PNG')
            buffer.seek(0)
            self.photo.save(self.photo.name, ContentFile(buffer.read()), save=False)

        super().save(*args, **kwargs)

    def resize_and_crop(self, image, size):
        # Resize the image without preserving the aspect ratio
        image = image.convert('RGB')
        image = image.resize(size)
        return image

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

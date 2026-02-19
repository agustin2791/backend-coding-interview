from photos.models import Photo
from django.core.management.base import BaseCommand
from api.settings import BASE_DIR
import pandas as pd

class Command(BaseCommand):
    help = ''
    def handle(self, *args, **options):
        '''A command line that imports data into the photo model/table from a csv. It currently imports from a file in files/photos.csv'''
        csv_file = f'{BASE_DIR}/files/photos.csv'
        df = pd.read_csv(csv_file)
        try:
            # Truncate photos table
            Photo.objects.all().delete()
            # import data from csv file
            for d in df.values:
                id,width,height,url,photographer,photographer_url,photographer_id,avg_color,original,large2x,large,medium,small,portrait,landscape,tiny,alt = d
                new_photo = Photo.objects.create(
                    id=id,
                    width=width,
                    height=height,
                    url=url,
                    photographer=photographer,
                    photographer_url=photographer_url,
                    photographer_id=photographer_id,
                    avg_color=avg_color,
                    original=original,
                    large2x=large2x,
                    large=large,
                    medium=medium,
                    small=small,
                    portrait=portrait,
                    landscape=landscape,
                    tiny=tiny,
                    alt=alt
                )
                new_photo.save()
        except:
            print('did not work')
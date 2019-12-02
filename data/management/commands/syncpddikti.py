import pyodbc

from django.core.management.base import BaseCommand
from django.utils import timezone
# from datetime import datetime

from pddikti.models import DataPT

PDDIKTI_QUERY = """
SELECT dbo.v_kuliah_mhs.last_sync, dbo.v_kuliah_mhs.id_smt,
dbo.v_kuliah_mhs.id_reg_pd, dbo.v_kuliah_mhs.id_stat_mhs
FROM dbo.v_kuliah_mhs
WHERE dbo.v_kuliah_mhs.last_sync >= Convert(datetime, '2019-10-30')
AND dbo.v_kuliah_mhs.id_stat_mhs <> 'A'
AND NOT CONVERT(int, dbo.v_kuliah_mhs.id_smt) >= 20181
"""

class Command(BaseCommand):
    help = 'Sync to PDDIKTI database...'

    def handle(self, *args, **kwargs):
        # Specifying timezone
        #jkt_tz = pytz.timezone("Asia/Jakarta")

        # Specifying the ODBC driver, server name, database, etc. directly
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.1.99.31;DATABASE=pddikti;UID=kopwil08;PWD=L2d1kti#18')

        # Create a cursor from the connection
        cursor = cnxn.cursor()
        cursor.execute(PDDIKTI_QUERY)
        rows = cursor.fetchall()
        for row in rows:
            d = DataPT(
                last_sync = row.last_sync,
                id_smt = str(row.id_smt),
                id_reg_pd = str(row.id_reg_pd),
                id_stat_mhs = str(row.id_stat_mhs)
            )
            d.save()
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

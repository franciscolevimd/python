# import pytz
from zoneinfo import ZoneInfo
from datetime import datetime, timezone
# Usar tzdata si no se tiene base de datos de zonas horarias.


reference_time = datetime.now(timezone.utc)
# print("Reference time (UTC):", reference_time)
# naive = datetime.now()
# print("Reference time (Local):", naive)

mexico = datetime.now(ZoneInfo("America/Mexico_City"))  # IANA code
colombia = datetime.now(ZoneInfo("America/Bogota"))
venezuela = datetime.now(ZoneInfo("America/Caracas"))
argentina = datetime.now(ZoneInfo("America/Argentina/Buenos_Aires"))

reference = datetime(1985, 6, 17, 13, 15, 25, tzinfo=timezone.utc)
mexico = reference.astimezone(ZoneInfo("America/Mexico_City"))
colombia = reference.astimezone(ZoneInfo("America/Bogota"))
venezuela = reference.astimezone(ZoneInfo("America/Caracas"))
argentina = reference.astimezone(ZoneInfo("America/Argentina/Buenos_Aires"))

breakpoint()  # pdb

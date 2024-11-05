from datetime import datetime, timezone
from zoneinfo import ZoneInfo

timestamp = 1730768627
dt_utc = datetime.fromtimestamp(timestamp, timezone.utc)

# Converter para o horário de Brasília
dt_brazil = dt_utc.astimezone(ZoneInfo("America/Sao_Paulo"))

print("UTC:", dt_utc)
print("Horário de Brasília:", dt_brazil)
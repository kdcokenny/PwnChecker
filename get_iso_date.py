from datetime import datetime, timezone

def get_iso_date():
    current_date = datetime.now(timezone.utc)
    date_timezone = current_date.astimezone()
    iso_dt_tz = date_timezone.isoformat()
    return iso_dt_tz

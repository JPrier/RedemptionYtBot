from datetime import datetime, timedelta

# Timestamp is in RFC3339 format
def addMinutesToTimestamp(timestamp, delta):
    # Parse the RFC 3339 timestamp
    parsedTimestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")

    # Add Delta
    updatedTimestamp = parsedTimestamp + timedelta(minutes=delta)

    # Convert back to RFC 3339 format
    return updatedTimestamp.strftime("%Y-%m-%dT%H:%M:%SZ")

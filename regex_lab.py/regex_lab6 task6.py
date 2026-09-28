import re

log = """2026-09-28 10:15:23 ERROR user=alice msg=Login failed
2026-09-28 10:16:10 INFO user=bob msg=Login successful
2026-09-28 10:17:45 WARN user=alice msg=Password expires soon
2026-09-28 10:18:30 ERROR user=charlie msg=File not found
2026-09-28 10:19:12 INFO user=alice msg=File uploaded
2026-09-28 10:20:05 ERROR user=bob msg=Permission denied
2026-09-28 10:21:15 WARN user=charlie msg=Low disk space
"""

# Regex with named groups
pattern = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(?P<level>ERROR|WARN|INFO) '
    r'user=(?P<user>\w+) '
    r'msg=(?P<msg>.*)'
)

# Use finditer() to parse log entries
entries = []

for match in pattern.finditer(log):
    entries.append(match.groupdict())

print("Parsed Entries:")
for entry in entries:
    print(entry)


# Summary count of ERROR, WARN and INFO
counts = {
    "ERROR": 0,
    "WARN": 0,
    "INFO": 0
}

for entry in entries:
    counts[entry["level"]] += 1

print("\nSummary:")
print("ERROR:", counts["ERROR"])
print("WARN:", counts["WARN"])
print("INFO:", counts["INFO"])


# Redact usernames
redacted_log = re.sub(
    r'user=\w+',
    'user=<hidden>',
    log
)

print("\nRedacted Log:")
print(redacted_log)


# Bonus: Sort entries by user name
sorted_entries = sorted(entries, key=lambda x: x["user"])

print("\nERROR entries for each user:")

current_user = None

for entry in sorted_entries:
    if entry["user"] != current_user:
        current_user = entry["user"]
        print("\nUser:", current_user)

    if entry["level"] == "ERROR":
        print(entry)
        #output
        #Parsed Entries:
#{'timestamp': '2026-09-28 10:15:23', 'level': 'ERROR', 'user': 'alice', 'msg': 'Login failed'}
#{'timestamp': '2026-09-28 10:16:10', 'level': 'INFO', 'user': 'bob', 'msg': 'Login successful'}
#{'timestamp': '2026-09-28 10:17:45', 'level': 'WARN', 'user': 'alice', 'msg': 'Password expires soon'}
#{'timestamp': '2026-09-28 10:18:30', 'level': 'ERROR', 'user': 'charlie', 'msg': 'File not found'}
#{'timestamp': '2026-09-28 10:19:12', 'level': 'INFO', 'user': 'alice', 'msg': 'File uploaded'}
#{'timestamp': '2026-09-28 10:20:05', 'level': 'ERROR', 'user': 'bob', 'msg': 'Permission denied'}
#{'timestamp': '2026-09-28 10:21:15', 'level': 'WARN', 'user': 'charlie', 'msg': 'Low disk space'}

Summary:
ERROR: 3
WARN: 2
INFO: 2


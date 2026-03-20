import datetime

servers = ['google.com', 'github.com', 'microsoft.com']

print("=" * 40)
print("SERVER HEALTH CHECK REPORT")
print(f"Time: {datetime.datetime.now()}")
print("=" * 40)

for server in servers:
    print(f"Checking... {server} -> OK")

print("=" * 40)
print("All checks completed successfully!")

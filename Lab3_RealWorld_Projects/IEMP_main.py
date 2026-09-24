from IEMP_telemetry import generate_telemetry, process_data
from IEMP_diagnostics import diagnostic, analyze_fault


LAST_NAME = "SABARIAGA"
SEED_NUM = 2
FAVORITE_ARTIST = "MICO"


data = generate_telemetry(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)

telemetry = list(data)

processed = process_data(telemetry)

valid, invalid, abnormal = diagnostic(processed)

print("Student:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

print("Generated Telemetry:", telemetry)
print("Processed Telemetry:", processed)

print("Valid Readings:", valid)
print("Invalid Readings:", invalid)
print("Abnormal Readings:", abnormal)

if len(abnormal) > 0:
    recursive_result = analyze_fault(abnormal[0])
else:
    recursive_result = 0

print("Recursive Analysis:", recursive_result)

print("Number of Processed Readings:", len(processed))
print("Number of Valid Readings:", len(valid))
print("Number of Invalid Readings:", len(invalid))
print("Number of Abnormal Conditions:", len(abnormal))

if len(abnormal) == 0 and len(invalid) == 0:
    status = "NORMAL"
else:
    status = "NEEDS ATTENTION"

print("Overall Equipment Status:", status)
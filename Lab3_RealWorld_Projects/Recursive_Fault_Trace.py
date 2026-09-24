# CODE 2

LAST_NAME = "SABARIAGA"
SEED_NUM = 2
FAVORITE_ARTIST = "MICO"


def generate_fault_code():
    code = sum(ord(c) for c in LAST_NAME)
    code += sum(ord(c) for c in FAVORITE_ARTIST)
    code += SEED_NUM
    return code


trace = []
call_count = 0


def trace_fault(code):
    global call_count

    call_count += 1
    trace.append(code)

    if code <= 10:
        return code

    return trace_fault(code - 10)


fault_code = generate_fault_code()
final_result = trace_fault(fault_code)

print("Generated Fault Data:", fault_code)
print("Recursive Trace:", trace)
print("Number of Recursive Calls:", call_count)
print("Final Result:", final_result)
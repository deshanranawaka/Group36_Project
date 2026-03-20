import re

log_file = "scaling_report.txt"

print(f"{'Scenario':<30} | {'Runtime (sec)':<15}")
print("-" * 50)

with open(log_file, "r") as f:
    content = f.read()
    # Split by scenario headers
    scenarios = re.split(r'SCENARIO: ', content)
    
    for section in scenarios[1:]:
        lines = section.strip().split('\n')
        name = lines[0]
        # Look for the "Total Runtime: X.XX seconds" line
        runtime_match = re.search(r'Total Runtime: ([\d.]+) seconds', section)
        
        if runtime_match:
            runtime = runtime_match.group(1)
            print(f"{name:<30} | {runtime:<15}")
        else:
            print(f"{name:<30} | Still Running/Failed")
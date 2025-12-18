import re
from collections import Counter
import sys

def analyze_log_file(log_file_path):
    """Analyzes a web server log file for 404s, popular pages, and top IPs."""

    # Simple regex to extract IP, Method, Path, and Status Code
    # This regex is simplified for demonstration purposes
    log_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"(GET|POST|HEAD)\s+(.*?)\s+HTTP.*? (\d{3})')

    # Counters to store data
    ip_counts = Counter()
    page_counts = Counter()
    total_404s = 0

    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                match = log_pattern.search(line)
                if match:
                    ip, _, path, status_code_str = match.groups()
                    status_code = int(status_code_str)

                    # 1. Count IPs and pages
                    ip_counts[ip] += 1
                    page_counts[path] += 1

                    # 2. Count 404 errors
                    if status_code == 404:
                        total_404s += 1
    except FileNotFoundError:
        print(f"Log file not found at : {log_file_path}")
        return
    
    # Generate report
    print("=========================================")
    print(f"    LOG ANALYSIS REPORT for: {log_file_path}")
    print("=========================================")

    # 1. 404 Errors
    print(f"\nTotal 404 (Not Found) Errors: {total_404s}")

    # 2. Most Requested Pages (Top 3)
    print("\nTop 3 Most Requested Pages:")
    for page, count in page_counts.most_common(3):
        print(f"  - {page}: {count} requests")

    # 3. Top IP Addresses (Top 3)
    print("\nTop 3 IP Addresses (Source of Most Requests):")
    for ip, count in ip_counts.most_common(3):
        print(f"  - {ip}: {count} requests")
    print("=========================================")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_log = sys.argv[1]
    else:
        target_log = "sample.log"

    analyze_log_file(target_log)
    
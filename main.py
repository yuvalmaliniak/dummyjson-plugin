from client import ApiClient
from data_collector import EvidenceCollector
import json

def main():
    client = ApiClient()
    try:
        client.authenticate()
        print("✅ Authenticated successfully.")
    except Exception as e:
        print("❌ Authentication failed:", e)
        return

    collector = EvidenceCollector(client)

    try:
        evidences = client.evidences_to_collect
        if evidences <= 0:
            print("No evidences to collect.")
            return
        for i in range(1, evidences + 1):
            method_name = f"collect_e{i}"
            try:
                if hasattr(collector, method_name):
                    method = getattr(collector, method_name)
                    result = method()
                    print(f"E{i} result:")
                    print(json.dumps(result, indent=2))
                else:
                    print(f"Method {method_name} not found.")
            except Exception as e:
                print(f"Error collecting E{i}: {e}")

    except Exception as e:
        print("Error collecting evidence:", e)

if __name__ == "__main__":
    main()

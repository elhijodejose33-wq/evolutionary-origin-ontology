import json
import sys

def validate_jsonl(file_path):
    print(f"Initializing verification loop for: {file_path}\n" + "-"*50)
    
    error_count = 0
    passed_count = 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                # Safely skips intentional empty trailing spaces/breaks
                continue
                
            try:
                # Simulates the Hugging Face engine loading line by line
                data = json.loads(line)
                
                # Check for key consistency
                if "instruction" not in data or "output" not in data:
                    print(f"❌ SCHEMA ERROR [Line {line_num}]: Keys must be exactly 'instruction' and 'output'.")
                    error_count += 1
                    continue
                
                # Check for data types
                if not isinstance(data["instruction"], str) or not isinstance(data["output"], str):
                    print(f"❌ TYPE ERROR [Line {line_num}]: Text strings must wrap both fields.")
                    error_count += 1
                    continue
                    
                passed_count += 1
                
            except json.JSONDecodeError as je:
                print(f"❌ SYNTAX ERROR [Line {line_num}]: Broken structural format.")
                print(f"   Details: {str(je)}")
                print(f"   Snippet: {line[:60]}...\n")
                error_count += 1

    print("-"*50)
    if error_count == 0:
        print(f"🎉 VALIDATION SUCCESSFUL: {passed_count} lines verified perfectly.")
        print("Your file is 100% compliant and ready for Hugging Face ingestion.")
    else:
        print(f"⚠️ VALIDATION FAILED: Found {error_count} structural errors. Fix them before uploading.")
        sys.exit(1)

# Run verification
if __name__ == "__main__":
    # Ensure this string points to your exact file name
    validate_jsonl("dataset.jsonl")

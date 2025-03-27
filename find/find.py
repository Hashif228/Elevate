import re
import csv

def extract_patterns(file_path):
    extracted_data = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                for match in re.findall(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}', line):
                    extracted_data[("email=>", match)] = extracted_data.get(("email", match), 0) + 1
                for match in re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line):
                    extracted_data[("ip", match)] = extracted_data.get(("ip=>", match), 0) + 1
                for match in re.findall(r'\b\d{4}[-/]\d{2}[-/]\d{2}\b', line):
                    extracted_data[("date", match)] = extracted_data.get(("date", match), 0) + 1
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    return extracted_data

def write_to_csv(data, output_file):
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Value", "Count"])
            for (data_type, value), count in data.items():
                writer.writerow([data_type, value, count])
    except Exception as e:
        print(f"Error writing CSV: {e}")

if __name__ == "__main__":
    file_path = "sample_text_file.txt" 
    output_csv = "output.csv"
    
    extracted_data = extract_patterns(file_path)
    
    if extracted_data:
        write_to_csv(extracted_data, output_csv)
        print("Extraction complete. Data saved to CSV.")

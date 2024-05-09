import csv

def write_to_txt_file(file_path, output):
    with open(file_path, 'w') as file:
        file.write(output)

def read_csv_file(input_file_path, output_file_path):
    try:
        output = ""
        with open(input_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                emplid = row.get('ï»¿Emplid')
                empl_rcd = row.get('Empl Rcd')
                position_id = row.get('Position ID')[:10]
                if emplid and empl_rcd and position_id:
                    output += f"Update asgnmt set computed_match_id = '{emplid}-{position_id}' where computed_match_id = '{emplid}-{empl_rcd}';\n"
                    output += f"Update ppi_asgnmt_stage set computed_match_id = '{emplid}-{position_id}' where computed_match_id = '{emplid}-{empl_rcd}';\n"
        
        write_to_txt_file(output_file_path, output)
        print(f"Output has been written to '{output_file_path}'.")
        
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

input_file_path = 'EMP_LIST.csv'
output_file_path = 'output.txt'
read_csv_file(input_file_path, output_file_path)
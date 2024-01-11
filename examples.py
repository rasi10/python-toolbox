from src.port_scanner import scan_ports
from src.services_scanner import services_services
from src.change_file_extensions import change_file_extension
from src.encrypt_decrypt_util import encrypt_string, decrypt_string


def main():
    pass
    #print('PORT SCANNER')
    #host = input("Enter the host IP to scan: ")
    #open_ports = scan_ports(host, 1, 500)

    #print('SERVICES SCANNER')
    #services_services()

    #print('CHANGE FILE EXTENSIONS')
    #change_file_extension('./test_files', 'csv', 'txt')


    #print('ENCRYPT AND DECRYPT STRINGS')
    #original_string = "This is a secret message."
    #encrypted_data = encrypt_string(original_string)
    #print(f"Encrypted: {encrypted_data}")    
    #decrypted_string = decrypt_string(encrypted_data)
    #print(f"Decrypted: {decrypted_string}")

if __name__ == "__main__":
    main()

from src.port_scanner import scan_ports
from src.services_scanner import services_scanner
from src.change_file_extensions import change_file_extension
from src.encrypt_decrypt_util import encrypt_string, decrypt_string


def main():    
    #pass
    # print('PORT SCANNER')
    # host = input("Enter the host IP to scan: ")
    # open_ports = scan_ports(host, 1, 10000)

    # print('SERVICES SCANNER')
    # services_scanner()

    print('CHANGE FILE EXTENSIONS')
    change_file_extension('./test_files', 'txt', 'csv')


    #print('ENCRYPT AND DECRYPT STRINGS')
    #original_string = "If you succeed decrypting this message, you will get a dumble!"
    #encrypted_data = encrypt_string(original_string)
    #print(f"Encrypted: {encrypted_data}")    
    #decrypted_string = decrypt_string(encrypted_data)
    #print(f"Decrypted: {decrypted_string}")

if __name__ == "__main__":
    main()

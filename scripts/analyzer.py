#TODO: chatgpt дал базу для нормального и красивого кода для анализа конфиг файлов. необходимо оформить это в виде функций,
# обеспечить взаимодействие с файлом nmap.py (описание для него написано в общий чертах), необходимо расширить список проверяемых пунктов 
# конфигурации, обеспечить список из мисконфигов, потом его выведем


# Check FTP server configuration
ftp_config_file = '/etc/vsftpd.conf'
with open(ftp_config_file, 'r') as f:
    ftp_config = f.read()
if 'anonymous_enable=YES' in ftp_config:
    print("FTP server is insecure. Anonymous login is enabled.")
else:
    print("FTP server is secure.")

# Check SSH server configuration
ssh_config_file = '/etc/ssh/sshd_config'
with open(ssh_config_file, 'r') as f:
    ssh_config = f.read()
if 'PermitRootLogin yes' in ssh_config:
    print("SSH server is insecure. Root login is enabled.")
else:
    print("SSH server is secure.")

# Check Apache server configuration
apache_config_file = '/etc/httpd/conf/httpd.conf'
with open(apache_config_file, 'r') as f:
    apache_config = f.read()
if 'ServerTokens Prod' in apache_config:
    print("Apache server is insecure. ServerTokens is set to Prod.")
else:
    print("Apache server is secure.")

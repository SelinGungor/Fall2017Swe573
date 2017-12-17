# import MySQLdb
# from sshtunnel import SSHTunnelForwarder
#
# with SSHTunnelForwarder(
#          ('ssh.pythonanywhere.com',22),
#          ssh_password="C@ndlepink",
#          ssh_username="selingungor",
#          remote_bind_address=('selingungor.mysql.pythonanywhere-services.com', 3306)) as server:
#
#     conn = MySQLdb.connect(host='selingungor.mysql.pythonanywhere-services.com',
#                            port=server.local_bind_port,
#                            user='selingungor',
#                            passwd='MyDeepYouP@ss',
#                            db='selingungor$deepyou')
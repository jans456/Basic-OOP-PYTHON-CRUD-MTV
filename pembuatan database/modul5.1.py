import mysql.connector as mysql

host="localhost"
user="root"
passwd=""

db = mysql.connect(
    host=host,
    user=user,
    passwd=passwd
)

cursor= db.cursor()
db.database = "pbo1"
cursor.execute('''
CREATE TABLE `dosen` (
  `id` int(11) UNSIGNED NOT NULL,
  `nidn` varchar(100) DEFAULT '',
  `nama` varchar(100) NOT NULL,
  `barang` varchar(100) DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
''')
db.commit()
cursor.execute("SHOW TABLES")
data = cursor.fetchall()
print(data)
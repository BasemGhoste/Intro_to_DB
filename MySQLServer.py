import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # الاتصال بخادم MySQL بدون تحديد قاعدة بيانات
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",     # استبدل باسم المستخدم الخاص بك
            password="your_password"  # استبدل بكلمة المرور الخاصة بك
        )
        cursor = connection.cursor()

        # إنشاء قاعدة البيانات إذا لم تكن موجودة
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # التعامل مع الأخطاء بشكل مفصل
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # التأكد من إغلاق الموارد
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    create_database()

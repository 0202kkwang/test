import mysql.connector

try:
    # 连接到 MySQL 数据库
    mydb = mysql.connector.connect(
        host="localhost",
        user=" root",
        password="123456"
    )
    mycursor = mydb.cursor()

    # 数据库操作：创建数据库
    mycursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
    print("数据库创建成功")

    # 使用数据库
    mycursor.execute("USE test_db")
    print("已使用 test_db 数据库")

    # 表操作：创建表
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT,
        email VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    mycursor.execute(create_table_query)
    print("表创建成功")

    # 表操作：修改表结构 - 添加列
    alter_table_add_column = "ALTER TABLE users ADD COLUMN address VARCHAR(200)"
    mycursor.execute(alter_table_add_column)
    print("表结构修改：添加列成功")

    # 表操作：修改表结构 - 修改列的数据类型
    alter_table_modify_column = "ALTER TABLE users MODIFY COLUMN age TINYINT"
    mycursor.execute(alter_table_modify_column)
    print("表结构修改：修改列数据类型成功")

    # 数据操作：插入数据
    insert_query = "INSERT INTO users (name, age, email, address) VALUES (%s, %s, %s, %s)"
    users = [
        ('John', 25, 'john@example.com', '123 Main St'),
        ('Alice', 22, 'alice@example.com', '456 Elm St'),
        ('Bob', 30, 'bob@example.com', '789 Oak St')
    ]
    mycursor.executemany(insert_query, users)
    mydb.commit()
    print(mycursor.rowcount, "条记录插入成功")

    # 数据操作：查询数据 - 简单查询
    mycursor.execute("SELECT * FROM users")
    results = mycursor.fetchall()
    print("简单查询结果：")
    for row in results:
        print(row)

    # 数据操作：查询数据 - 条件查询
    mycursor.execute("SELECT * FROM users WHERE age > 22")
    results = mycursor.fetchall()
    print("条件查询结果：")
    for row in results:
        print(row)

    # 数据操作：查询数据 - 排序查询
    mycursor.execute("SELECT * FROM users ORDER BY age DESC")
    results = mycursor.fetchall()
    print("排序查询结果：")
    for row in results:
        print(row)

    # 数据操作：查询数据 - 分页查询
    mycursor.execute("SELECT * FROM users LIMIT 2 OFFSET 1")
    results = mycursor.fetchall()
    print("分页查询结果：")
    for row in results:
        print(row)

    # 数据操作：更新数据
    update_query = "UPDATE users SET age = 26 WHERE name = 'John'"
    mycursor.execute(update_query)
    mydb.commit()
    print(mycursor.rowcount, "条记录更新成功")

    # 数据操作：删除数据
    delete_query = "DELETE FROM users WHERE name = 'Bob'"
    mycursor.execute(delete_query)
    mydb.commit()
    print(mycursor.rowcount, "条记录删除成功")

    # 再次查询数据，查看删除和更新后的结果
    mycursor.execute("SELECT * FROM users")
    results = mycursor.fetchall()
    print("更新和删除后的查询结果：")
    for row in results:
        print(row)

    # 表操作：删除表
    mycursor.execute("DROP TABLE IF EXISTS users")
    print("表删除成功")

    # 数据库操作：删除数据库
    mycursor.execute("DROP DATABASE IF EXISTS test_db")
    print("数据库删除成功")

except mysql.connector.Error as err:
    print(f"发生错误: {err}")
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("数据库连接已关闭")


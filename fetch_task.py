from flask import session
from flask import Blueprint
from connect import connectDB
from connect import DB_NAME,TASK_ID_TABLE, USER_ID_TABLE

def fetchAll(taskType,sortBy,search_key,tableName = TASK_ID_TABLE):
    if taskType == None:
        taskType="all"
    if sortBy == None:
        sortBy="default"
    print(taskType)
    print(sortBy)
    conn = connectDB()
    cur = conn.cursor()

    query1= f"""
    SELECT * FROM {tableName}
    
    """
    has_where = False
    
    if taskType !="all":
        query1 += f"""
        WHERE `{taskType}`= "{session.get("username")}"
        """
        has_where = True
        
    if search_key and search_key not in ["None", ""]:
        print("Searching for:", search_key)
        if has_where:
            query1 += f"""
        AND `task_name` LIKE "{search_key}%"
        """
        else:
            query1 += f"""
        WHERE `task_name` LIKE "{search_key}%"
        """
        has_where = True
        
    if sortBy !="default":
        query1+=f"ORDER BY `{sortBy}` DESC"

    cur.execute(query1)
    output = cur.fetchall()
    
    return output

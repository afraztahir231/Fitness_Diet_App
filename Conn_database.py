import cx_Oracle
from datetime import date
def login_attempt_user(UserID,Pass):
    conn=cx_Oracle.connect('fitnessapp/123@//localhost:1522/XE')

    curr=conn.cursor()
    seach_query="""
    select count(*) from userr where ID=:1 and pass=:2 
    """
    curr.execute(seach_query,(UserID,Pass))
    results=curr.fetchall()
    curr.close()
    conn.close()
    if results[0][0]==0:
        return False
    else:
        return True

def login_attempt_trainer(UserID,Pass):
    conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 

    curr=conn.cursor()
    seach_query="""
    select count(*) from trainer where ID=:1 and pass=:2 
    """
    curr.execute(seach_query,(UserID,Pass))
    results=curr.fetchall()
    curr.close()
    conn.close()
    if results[0][0]==0:
        return False
    else:
        return True

#Provided a data
def fetch_user_data(userID):
    conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 
    curr=conn.cursor()
    curr.execute("select * from userr where ID=:myvar",myvar=userID)
    results=curr.fetchall()
    curr.close()
    conn.close()
    return results

def fetch_trainer_data(userID):
    conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 
    curr=conn.cursor()
    curr.execute("select * from trainer where ID=:myvar ",myvar=userID)
    results=curr.fetchall()
    curr.close()
    conn.close()
    return results


def insert_trainer(user_id,name,password,age,address,email,phone):
    try:
        conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 
        curr=conn.cursor()
        insert_query="""
        insert into trainer(id,name,pass,age,address,email,phonenumber,hiredate,monthlysalary) values(:1,:2,:3,:4,:5,:6,:7,:8,:9)
        """
        curr.execute(insert_query,(user_id,name,password,age,address,email,phone,date.today(),20000))
        conn.commit()
    except Exception as err:
        print("Can not insert Data")
        print(err)
        if (conn):
            curr.close()
            conn.close()
            return False
    else:
        if (conn):
            curr.close()
            conn.close()
            return True

def insert_user(user_id,name,password,age,weight,address,email,phone,foodpref):
    try:
        conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 
        curr=conn.cursor()
        insert_query="""
        insert into userr(id,name,pass,age,weight,address,email,phonenumber,foodpreference) values(:1,:2,:3,:4,:5,:6,:7,:8,:9)
        """
        curr.execute(insert_query,(user_id,name,password,age,weight,address,email,phone,foodpref))
        conn.commit()
    except Exception as err:
        print("Can not insert Data")
        print(err)
        if (conn):
            curr.close()
            conn.close()
            return False
    else:
        if (conn):
            curr.close()
            conn.close()
            return True


def trainer_info(ID):
    try:
        conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 
        curr=conn.cursor()
        curr.execute("select count(*) from user_trainer where trainerid=:myvar",myvar=ID)
        total_customers=curr.fetchall()
        total_customers=total_customers[0][0]
        conn.commit()
        other_info=fetch_trainer_data(ID)
        other_info=other_info[0]
    except Exception as err:
        print("Can not extract Data")
        print(err)
        if (conn):
            curr.close()
            conn.close()
            return [None,None,None,None,None,None]
    else:
        if (conn):
            curr.close()
            conn.close()
            return[str(other_info[0]),str(other_info[1]),str(other_info[7]),str(total_customers),str(other_info[8]),str(other_info[8]*total_customers)]


def get_current_day_workout():
    try:
        weekdays={
            1:'monday',
            2:'tuesday',
            3:'wednesday',
            4:'thursday',
            5:'friday',
            6:'saturday',
            7:'sunday',
        }
        today=date.today().isoweekday()
        conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 
        curr=conn.cursor()
        curr.execute("select * from workout where day=:myvar",myvar=weekdays[today])
        result=curr.fetchall()
    except Exception as err:
        print("Error Could not Compute Workout Routine!")
        print(err)
        if(conn):
            curr.close()
            conn.close()
            return [None,None,None,None,None,None,None,None]
    else:
        if (conn):
            curr.close()
            conn.close()
            return [result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7],result[0][8]]


def generate_reciept(userID,mealType):
    try:
        userinformation=fetch_user_data(userID)#tuple within a list here
        conn=cx_Oracle.connect('FITNESSAPP/123@//localhost:1522/xe') 
        curr=conn.cursor()

        counting_total_reciepts="""
        select count(*) from receipt
        """
        curr.execute(counting_total_reciepts)
        cnt=curr.fetchall()
        cnt=cnt[0][0]+1 # here we generate a unique rreciept number
        generate_reciept="""
        insert into receipt (order_id,user_id,meal_type,order_date) values(:1,:2,:3,:4)
        """
        weekdays={
            1:'monday',
            2:'tuesday',
            3:'wednesday',
            4:'thursday',
            5:'friday',
            6:'saturday',
            7:'sunday'
        }
        userFoodPref=userinformation[0][8]
#getting food items and total price
        curr.execute(generate_reciept,(int(cnt),userID,mealType,date.today()))
        conn.commit()
        curr.execute('select item1,item2,item3 from diet where meal_type=:usrmt and diet_type=:usrdt',usrmt=mealType,usrdt=userFoodPref)
        result=curr.fetchall()
        fooditems=result[0][0]+" "+result[0][1]+" "+result[0][2]
        curr.execute('select total_price from food_pricing where meal_type=:usrmt and diet_type=:usrdt',usrmt=mealType,usrdt=userFoodPref)
        result=curr.fetchall()
        total_price=result[0][0]
    
    except Exception as err:
        print("could not generate Receipt")
        print(err)
        if (conn):
            curr.close()
            conn.close()
            return [None,None,None,None,None,None,None,None,None,None]
    else:
        if (conn):
            curr.close()
            conn.close()
            return [userinformation[0][1],userID,weekdays[date.today().isoweekday()],date.today(),cnt,mealType,fooditems,userinformation[0][8],total_price,userinformation[0][5]]


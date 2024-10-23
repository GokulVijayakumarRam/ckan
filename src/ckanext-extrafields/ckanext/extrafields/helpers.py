import logging
import mysql.connector
import flask
from flask import Flask, request, jsonify
def extrafields_hello():
    return "Hello, extrafields!"


def staff_list_fetch( input_val  ):
    logging.warning("I got here")
    try:
        mydb = mysql.connector.connect(
            host="promessa.rothamsted.ac.uk",
            user="pma_user",
            password="t5[2E;P!NTbs",
            database="CKAN"
        )
        print("Connection successful")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    # input_val = "rich"
    logging.warning(input_val)
    mycursor = mydb.cursor()
    query = "SELECT * FROM `ckanstafflist` WHERE `fullname` LIKE %s"
    mycursor.execute(query, ('%' + input_val + '%',))
    myresult = mycursor.fetchall()

    logging.warning(myresult)
        
    return 


   

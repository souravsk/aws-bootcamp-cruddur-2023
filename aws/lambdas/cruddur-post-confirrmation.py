import json
import psycopg2
import os


def lambda_handler(event, context):
    user = event['request']['userAttributes']
    user_display_name = user['name']
    user_email = user['email']
    user_handle = user['preferred_username']
    user_cognito_id = user['sub']
    
    try:
        sql = """
            INSERT INTO public.users (
                display_name, 
                email,
                handle, 
                cognito_user_id
            ) 
            VALUES (%s, %s, %s, %s)
        """
        
        params = [
            user_display_name,
            user_email,
            user_handle,
            user_cognito_id
        ]
        
        with psycopg2.connect(os.getenv('CONNECTION_URL')) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    else:
        print("Data inserted successfully")
    finally:
        print('Database connection closed.')
    
    return event
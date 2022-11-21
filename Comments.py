from SQLConnect import Connect

cur = Connect()
cursor = cur.con.cursor()


def create_comment(comment, user_id):
    sql = f"""
            INSERT INTO COMMENTS (comment, usuario_id) VALUES ('{comment}', {user_id})
           """
    cursor.execute(sql)
    cur.con.commit()
    cursor.close()


def view_comments():
    pass


def view_list_comments_admin():
    pass

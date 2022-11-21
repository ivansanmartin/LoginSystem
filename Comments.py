from SQLConnect import Connect

cur = Connect()
cursor = cur.con.cursor()


def create_comment(comment, user_id):
    sql = f"""
            INSERT INTO COMMENTS (comment, usuario_id) VALUES ('{comment}', {user_id})
           """
    cursor.execute(sql)
    cur.con.commit()


def view_comments(user_id):
    sql = f"""SELECT comment FROM COMMENTS WHERE usuario_id = {user_id}"""
    cursor.execute(sql)
    comments_user = cursor.fetchall()

    # Obtener cantidad de comentarios, numero.

    sql_comments = f"""SELECT usuario_id FROM COMMENTS WHERE usuario_id = {user_id}"""
    cursor.execute(sql_comments)
    get_comments = cursor.fetchall()

    total_comments = 0
    for sum_comments in get_comments:
        if sum_comments[0] == sum_comments[0]:
            total_comments += 1

    for comments in comments_user:
        print("- ", comments[0])

    print(f"\nTienes un total de \"{total_comments}\" comentarios.")


def view_list_comments_admin():
    pass

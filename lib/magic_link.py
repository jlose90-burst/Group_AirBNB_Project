import secrets

def create_code(connection, user_id, booking_id=None, hours=24):
    code = secrets.token_urlsafe(4)
    connection.execute(
        "INSERT INTO magic_links (code, user_id, booking_id, expires_at) "
        "VALUES (%s, %s, %s, NOW() + make_interval(hours => %s))",
        [code, user_id, booking_id, hours]
    )
    return code

def use_code(connection, code):
    rows = connection.execute(
        "SELECT user_id, booking_id FROM magic_links WHERE code = %s AND expires_at > NOW()",
        [code]
    )
    return rows[0] if rows else None
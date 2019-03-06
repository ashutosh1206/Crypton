import asyncore, socket, json, sqlite3, time

FLAG1 = "flag{XXXXXXXXXXX}"
POINT_TRESHOLD = 200

def json_response(code, additional_parameter=""):
    response_codes = {
        0 : "Point added",
        1 : "Collision found",
        2 : "Point already included",
        3 : 'Wrong input format. Please provide a string like this: {"x": val, "y": val, "c": val, "d": val, "groupID": val})',
        4 : "Value mismatch! X != c*P + d*Q",
        5 : "Server Error"
    }
    return '{"Response": "%d", "Message": "%s"%s}' % (code, response_codes[code], additional_parameter)


# Teams should choose a non-guessable groupID
def get_response(x, y, c, d, groupID):
    # open connection to database
    conn = sqlite3.connect("points.db")
    conn.row_factory = sqlite3.Row
    conn_cursor = conn.cursor()

    # convert sage integers to string to avoid "Python int too large for SQLite INTEGER"
    x = str(x)
    y = str(y)
    c = str(c)
    d = str(d)

    # Select records that map to the same X value
    conn_cursor.execute("SELECT * FROM points WHERE x = :x", {"x": x})
    query = conn_cursor.fetchall()

    # No record found -> Point is not yet included
    if len(query) == 0:
        # Insert point into database
        conn_cursor.execute("INSERT INTO points (x, y, c, d, groupID) VALUES (?, ?, ?, ?, ?)",
                  (x, y, c, d, groupID))
        # Get number of points added by this group
        conn_cursor.execute("SELECT x FROM points WHERE groupID = :gID", {"gID": groupID})
        points_found = conn_cursor.fetchall()
        add_param = ', "points_found": %d' % len(points_found)
        # When they found POINT_TRESHOLD distinguished points and a collision occured, return the colliding values as well
        if len(points_found) > POINT_TRESHOLD:
            add_param += ', "flag1": "%s"' % FLAG1
            if server.collision_found:
                # compute x from the collision, second flag is just x (not in flag format)
                add_param += ', "collision": %s' % (server.collision)
        response = json_response(0, add_param)
    else:
        # One (or more) records found -> check if they have the same exponents
        is_included = False
        for row in query:
            if row["c"] == c and row["d"] == d:
                is_included = True
                response = json_response(2)
                break

        if not is_included:
            # Exponents are different -> Collision found, add this point
            conn_cursor.execute("INSERT INTO points (x, y, c, d, groupID, collision) VALUES (?, ?, ?, ?, ?, 1)",
                      (x, y, c, d, groupID))
            # Get number of points added by this group
            conn_cursor.execute("SELECT x FROM points WHERE groupID = :gID", {"gID": groupID})
            points_found = conn_cursor.fetchall()
            add_param = ', "points_found": %d' % len(points_found)
            # add collision
            server.collision_found = True
            server.collision = '{"c_1": %s, "d_1": %s, "c_2": %s, "d_2": %s}' % (c, d, row["c"], row["d"])
            if len(points_found) > POINT_TRESHOLD:
                add_param += ', "collision": %s' % (server.collision)
            else:
                add_param += ', "collision": "collision found but not enough distinguished points submitted yet"'

            response = json_response(1, add_param + ', "c": %s, "d": %s' % (row["c"], row["d"]))

    # close db connection and return response
    conn.commit()
    conn_cursor.close()
    conn.close()
    return response


class DLogHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        try:
            json_data = self.recv(8192)
            if not json_data:
                return

            data = json.loads(json_data)
            # check if the format is correct
            if not ("x" in data and "y" in data and "c" in data and "d" in data and "groupID" in data):
                response = json_response(3)
            else:
                c = Integer(data["c"])
                d = Integer(data["d"])
                x = Integer(data["x"])
                y = Integer(data["y"])
                X = E((x, y))
                if X == c*P + d*Q:
                    response = get_response(data["x"], data["y"], data["c"], data["d"], data["groupID"])
                else:
                    print("expected %s = %d*%s + %d*%s, but got %s" % (c*P + d*Q, c, P, d, Q, X))
                    response = json_response(4)

            self.send(response)

        except Exception as e:
            response = json_response(5, ', "Error Message": "%s"' % e)


class Server(asyncore.dispatcher_with_send):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        # variable to store some collision
        self.collision_found = False
        self.collision = {}

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print("incoming connection from %s" % repr(addr))
            DLogHandler(sock)


if __name__ == '__main__':

    load("parameters.sage")
    server = Server(serverAdress, serverPort)
    asyncore.loop()

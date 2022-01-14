import connection

def add_portal(g_map, g_zoneid, g_areaid, g_px, g_py, g_pz, g_o, gt_displayid, gt_name, gt_data0):
    mydb = connection.create_connection()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `gameobject` ORDER BY `id` DESC LIMIT 1")

    biggest = mycursor.fetchall()




add_portal(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
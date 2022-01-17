import connection


def add_portal(g_map, g_zoneId, g_areaid, g_px, g_py, g_pz, g_o, gt_displayid, gt_name, gt_data0):
    mydb = connection.create_connection()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `gameobject` ORDER BY `id` DESC LIMIT 1")

    biggest = mycursor.fetchall()[0]
    g_guid = biggest[0] + 1
    g_id = biggest[1] + 1
    new_g = "INSERT INTO `gameobject` (guid, id, map, zoneId, areaId, spawnMask, phaseMask, position_x, position_y, position_z, orientation, rotation0, rotation1, rotation2, rotation3, spawntimesecs, animprogress, state, ScriptName, VerifiedBuild) " \
            "VALUES (" + str(g_guid) + "," + str(
        g_id) + "," + g_map + "," + g_zoneId + "," + g_areaid + "," + "1," + "1," + g_px + "," + g_py + "," + g_pz + "," + g_o + "," + "0,0,0,0,300,100,1,\"\",0" + ")"

    new_gt = "INSERT INTO `gameobject_template` (entry, type, displayId, name, IconName, castBarCaption, unk1, size, Data0, Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8, Data9, Data10, Data11, Data12, Data13, Data14, Data15, Data16, Data17, Data18, Data19, Data20, Data21, Data22, Data23, AIName, ScriptName, VerifiedBuild) " \
             "VALUES (" + str(g_id) + "," + "22," + gt_displayid + "," + "'" + gt_name + "'" + ",\"\",\"\",\"\",1," + gt_data0 + "," + "".join(['0,' for i in range(23)]) + "\"\",\"\",12340" + ")"

    mycursor.execute(new_g)
    mycursor.execute(new_gt)

add_portal(g_map = '0',
           g_zoneId = '1519',
           g_areaid = '0',
           g_px = '-8553.48',
           g_py = '1023.3',
           g_pz = '89.7311',
           g_o = '4.83883',
           gt_displayid = '7146',
           gt_data0 = '33728',
           gt_name = 'Portal to Shattrath')

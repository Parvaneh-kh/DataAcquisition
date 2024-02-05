from tkinter import *
from tkinter import filedialog
import pandas as pd
import mysql.connector
from tkinter import messagebox
import myframe
import webbrowser
import settinf
import groupset
import mytree
import typeset


FONT2 = ("Arial", 20, "italic")
# FONTEN = ("Arial", 10)
# FONTENBIG = ("Arial", 16)
# FONTENMED = ("Arial", 13)
BACKCOLOR = "#FF6000"
FRONTCOLOR = "#454545"
FRONTCOLORM = "#FF6000"

mydb = mysql.connector.connect(
    user='root',
    password='Mysql123',
    host='localhost',
    auth_plugin='mysql_native_password',
    database='bgatedata'
)
my_cursor = mydb.cursor(buffered=True)


def create_db():
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS `bgatedata`;")
    mydb.commit()
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS `types` ( `type_id` int NOT NULL AUTO_INCREMENT,`type_name` "
                      "varchar(45) NOT NULL,`Desc` varchar(120) DEFAULT NULL,  PRIMARY KEY (`type_id`))\
    ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
    mydb.commit()

    my_cursor = mydb.cursor()
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS `groups` (`group_id` int NOT NULL AUTO_INCREMENT,`group_name` varchar(45) NOT NULL,"
        "`Desc` varchar(120) DEFAULT NULL, PRIMARY KEY (`group_id`)) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT"
        " CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
    mydb.commit()

    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS `products` (`Id` int NOT NULL AUTO_INCREMENT,`group_id` int "
                      "DEFAULT NULL,`type_id` int DEFAULT NULL,\
    `fw_id` varchar(40) DEFAULT NULL,`Serial_num` varchar(45) DEFAULT NULL,`Passive_tag` varchar(45) DEFAULT NULL,"
                      "`Address` varchar(45) DEFAULT NULL,\
    `Method` tinyint DEFAULT NULL,`Status` int DEFAULT NULL,`signal` int DEFAULT NULL,"
                      "`Location` varchar(45) DEFAULT NULL,\
    `lastseen` datetime DEFAULT NULL,`group_name` varchar(45) DEFAULT NULL,`type_name` varchar(45) DEFAULT NULL,"
                      "`Number` int DEFAULT NULL,`RSSI` int DEFAULT NULL,`Battery` int DEFAULT NULL,"
                      "`frame` varchar(100) DEFAULT NULL,`active` int DEFAULT '0',\
    PRIMARY KEY (`Id`)) ENGINE=InnoDB AUTO_INCREMENT=949 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
    mydb.commit()
    my_cursor = mydb.cursor()
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS `fw_ver` (`fw_id` int NOT NULL AUTO_INCREMENT,`fw_name` varchar(45) NOT NULL,"
        "`fw` varchar(60) NOT NULL,`fw_desc` varchar(120) DEFAULT NULL,PRIMARY KEY (`fw_id`)) "
        "ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
    mydb.commit()
    my_cursor = mydb.cursor()
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS`frames` (`Id` int NOT NULL,`frame` varchar(100) DEFAULT NULL,`date` datetime "
        "DEFAULT NULL,`Desc` "
        "varchar(100) DEFAULT NULL,`priority` int DEFAULT NULL,`port` varchar(10) DEFAULT NULL,`brate` int DEFAULT NULL"
        ",`bsize` int DEFAULT NULL,`stopbit` int DEFAULT NULL,`timeout` int DEFAULT NULL,`type` tinyint DEFAULT NULL,"
        " `interval` int DEFAULT NULL,PRIMARY KEY (`Id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 "
        "COLLATE=utf8mb4_0900_ai_ci;")
    mydb.commit()


def frameclear():
    group_button['background'] = FRONTCOLOR
    group_button['foreground'] = BACKCOLOR
    type_button['background'] = FRONTCOLOR
    type_button['foreground'] = BACKCOLOR
    setting_button['background'] = FRONTCOLOR
    setting_button['foreground'] = BACKCOLOR
    main_button['background'] = FRONTCOLOR
    main_button['foreground'] = BACKCOLOR
    import_button['background'] = FRONTCOLOR
    import_button['foreground'] = BACKCOLOR
    export_button['background'] = FRONTCOLOR
    export_button['foreground'] = BACKCOLOR

    f2.grid_forget()
    frame_setting.grid_forget()
    frame_group.grid_forget()
    frame_type.grid_forget()


def callsetting():
    frameclear()
    frame_setting.grid(row=1, column=1)
    settinf.Settingport(frame_setting)
    setting_button['background'] = BACKCOLOR
    setting_button['foreground'] = FRONTCOLOR


def firmname():
    mydb = mysql.connector.connect(
        user='root',
        password='Mysql123',
        host='localhost',
        auth_plugin='mysql_native_password',
        database='bgatedata'
    )
    cursor_1 = mydb.cursor(buffered=True)
    cursor_1.execute("SELECT `frame`.`frame` FROM bgatedata.frame where `frame`.`priority` = 1 and `frame`.`type` = 0;")
    record = cursor_1.fetchone()
    if record:
        return record[0]
    else:
        return ""


def dashboard():
    frameclear()
    fname = firmname()
    mt.frimlabel.config(text=fname)
    f2.grid(row=1, column=1)
    main_button['background'] = BACKCOLOR
    main_button['foreground'] = FRONTCOLOR


def call_hlink():
    webbrowser.open("https://www.nltinc.com/")


def group_form():
    # label_display.config(text="Groups form")
    frameclear()
    frame_group.grid(row=1, column=1)
    groupset.Settinggroup(frame_group)
    group_button['background'] = BACKCOLOR
    group_button['foreground'] = FRONTCOLOR


def type_form():
    # label_display.config(text="Types form")
    frameclear()
    frame_type.grid(row=1, column=1)
    typeset.Settingtype(frame_type)
    type_button['background'] = BACKCOLOR
    type_button['foreground'] = FRONTCOLOR

# def on_enter_main(e):
#     main_button['background'] = BACKCOLOR
#     main_button['foreground'] = FRONTCOLOR


# def on_leave_main(e):
#
#     if button_act[0]:
#         main_button['background'] = FRONTCOLOR
#         main_button['foreground'] = BACKCOLOR
#     else:
#         main_button['background'] = BACKCOLOR
#         main_button['foreground'] = FRONTCOLOR


def on_enter_frame(e):
    setting_button['background'] = BACKCOLOR
    setting_button['foreground'] = FRONTCOLOR

# def on_leave_frame(e):
#
#     if button_act[1]:
#         setting_button['background'] = BACKCOLOR
#         setting_button['foreground'] = FRONTCOLOR
#     else:
#         setting_button['background'] = FRONTCOLOR
#         setting_button['foreground'] = BACKCOLOR

def on_enter_import(e):
    import_button['background'] = BACKCOLOR
    import_button['foreground'] = FRONTCOLOR


# def on_leave_import(e):
#
#     if button_act[2]:
#         import_button['background'] = BACKCOLOR
#         import_button['foreground'] = FRONTCOLOR
#     else:
#         import_button['background'] = FRONTCOLOR
#         import_button['foreground'] = BACKCOLOR


def on_enter_export(e):
    export_button['background'] = BACKCOLOR
    export_button['foreground'] = FRONTCOLOR

# def on_leave_export(e):
#
#     if button_act[3]:
#         export_button['background'] = BACKCOLOR
#         export_button['foreground'] = FRONTCOLOR
#     else:
#         export_button['background'] = FRONTCOLOR
#         export_button['foreground'] = BACKCOLOR

#
# def on_enter_group(e):
#     if button_act[4]:
#         group_button['background'] = BACKCOLOR
#         group_button['foreground'] = FRONTCOLOR
#     else:
#         group_button['background'] = FRONTCOLOR
#         group_button['foreground'] = BACKCOLOR


# def on_leave_group(e):
#     reset(4)
#     if button_act[4]:
#         group_button['background'] = BACKCOLOR
#         group_button['foreground'] = FRONTCOLOR
#     else:
#         group_button['background'] = FRONTCOLOR
#         group_button['foreground'] = BACKCOLOR

def on_enter_type(e):
    type_button['background'] = BACKCOLOR
    type_button['foreground'] = FRONTCOLOR


# def on_leave_type(e):
#     if button_act[5]:
#         type_button['background'] = BACKCOLOR
#         type_button['foreground'] = FRONTCOLOR
#     else:
#         type_button['background'] = FRONTCOLOR
#         type_button['foreground'] = BACKCOLOR


def on_enter_exit(e):
    exit_button['background'] = BACKCOLOR
    exit_button['foreground'] = FRONTCOLOR


def on_leave_exit(e):
    exit_button['background'] = FRONTCOLOR
    exit_button['foreground'] = BACKCOLOR

def cont(val):
    # To convert nan value in excel to None
    if pd.isna(val):
        return None
    else:
        return val

def import_csv():
    frameclear()
    import_button['background'] = BACKCOLOR
    import_button['foreground'] = FRONTCOLOR
    # button_act[2] = True
    f2.filename = filedialog.askopenfilename(initialdir="/archive_files", title="Select a file :",
                                             filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    if f2.filename != "":
        my_cursor = mydb.cursor()
        sql_command = "SELECT Address FROM bgatedata.products"
        my_cursor.execute(sql_command)
        macs_list = [i[0] for i in my_cursor.fetchall()]

        df = pd.read_excel(f2.filename)
        rec_list = []
        for index, row in df.iterrows():
            rec_list.append(row.to_list())
        for row in rec_list:
            find_add = [index for index, item in enumerate(macs_list) if item == row[3]]
            if len(find_add) == 0:
                sql_command = (
                    "INSERT INTO bgatedata.products (group_name,type_name,Address,Serial_num,Status,Battery,RSSI,"
                    "lastseen,frame,Passive_tag,Location,Active) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
                values = (cont(row[0]), cont(row[1]), cont(row[3]), cont(row[2]), cont(row[6]), cont(row[7]),
                          cont(row[8]), cont(row[5]), cont(row[4]), cont(row[10]), cont(row[9]), 1)
            else:
                sql_command = ("UPDATE `bgatedata`.`products` set  group_name= %s,type_name= %s,Serial_num = %s,"
                               "Status = %s,Battery = %s ,RSSI = %s, lastseen = %s, frame =%s ,Passive_tag=%s,"
                               "location=%s,`active`=1 where Address = %s;")
                values = (cont(row[0]), cont(row[1]), cont(row[2]), cont(row[6]), cont(row[7]), cont(row[8]),
                          cont(row[5]), cont(row[4]), cont(row[10]), cont(row[9]), cont(row[3]))
            my_cursor.execute(sql_command, values)
            mydb.commit()
        messagebox.showwarning("Import ", "Import is completed restart application please !")
    import_button['background'] = FRONTCOLOR
    import_button['foreground'] = BACKCOLOR
        # now = datetime.now()
        # if not os.path.exists("Log_Files/"):
        #     os.makedirs("Log_Files/")
        # log_file = "Log_Files/" + now.strftime("%Y-%m-%d") + ".csv"
        # with open(log_file, 'a') as myfile:
            # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            # writer_csv = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            # writer_csv.writerows(same_mac)
        # myfile.close()

def export_csv():
    frameclear()
    export_button['background'] = BACKCOLOR
    export_button['foreground'] = FRONTCOLOR
    # button_act[3] = True
    f2.filename = filedialog.asksaveasfilename(initialdir="/archive_files", title="Select a file :",
                                               filetypes=(("Excel file", "*.xlsx"), ("csv files", "*.csv")))
    if f2.filename != "":
        sql = ("SELECT `products`.`group_name`,`products`.`type_name`,`products`.`Serial_num`,`products`.`Address`,"
               "`products`.`fw_id`,`products`.`lastseen`,`products`.`Status`,`products`.`Battery`,`products`.`RSSI`,"
               "`products`.`Location`,`products`.`Passive_tag`,`products`.`Id` FROM `bgatedata`.`products`;")
        df = pd.read_sql(sql, mydb)
        df.head()
        df.to_excel(f2.filename + ".xlsx", index=False)
    export_button['background'] = FRONTCOLOR
    export_button['foreground'] = BACKCOLOR


def exit_door():
    if mt.main_close:
        mt.auto_scan = False
        mt.auto_scan_start()
    w.quit()
# w = Tk()
# w.iconbitmap('./nlt.ico')
# w.configure(bg="#454545")
# # w.resizable(0,0)
# w.title("Orange Gate ")
# f2 = Frame(w, width=1450, height=750, bg=BACKCOLOR, padx=2, pady=2)
# f2.grid(row=1, column=1, rowspan=2)
# tree_frame = Frame(f2)
# tree_frame.grid(row=0, columnspan=2)
# mt = mytree.TreeviewCreate(tree_frame)
# create_db()
# settinf.port_reader()
# firma = firmname()
# mt.frimlabel.config(text=firma)

if __name__ == "__main__":
    w = Tk()
    app_width = 1400
    app_height = 780
    # font_reg = Font(family="Arial", size=20, slant="italic")
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x = abs(round((screen_width/2) - (app_width/2)))
    y = round((screen_height/2) - (app_height/2))-44
    w.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    # style = ttk.Style()
    w.iconbitmap('./nlt.ico')
    w.configure(bg="#454545")
    # w.resizable(0,0)
    w.title("Orange Gate 1.2 ")
    frame_main_2 = Frame(w, width=1200, height=30, bg=FRONTCOLOR)
    frame_main_2.grid(row=0, column=1)
    f2 = Frame(w, width=1550, height=750, bg=BACKCOLOR, padx=3, pady=3)
    # f2.grid(row=1, column=1, rowspan=2)
    f2.grid(row=1, column=1)
    tree_frame = Frame(f2)
    # tree_frame.grid(row=0, columnspan=2)
    tree_frame.grid(row=0, column=0)
    frame_setting = Frame(w, width=700, height=250, bg="#FF6000", padx=5, pady=5)
    frame_group = Frame(w, width=700, height=250, bg="#FF6000", padx=5, pady=5)
    frame_type = Frame(w, width=700, height=250, bg="#FF6000", padx=5, pady=5)
    app = myframe.HamburgerMenu(w)
    main_button = Button(app.menu_options_frame, text="Main", width=8, relief='flat', bg=BACKCOLOR, fg=FRONTCOLOR,
                           font=FONT2, command=dashboard)
    main_button.grid(row=1, column=0)
    setting_button = Button(app.menu_options_frame, text="Setting", width=8, relief='flat', bg=FRONTCOLOR, fg=BACKCOLOR,
                           font=FONT2, command=callsetting)
    setting_button.grid(row=2, column=0)
    import_button = Button(app.menu_options_frame, text="Import", width=8, relief='flat', bg=FRONTCOLOR, fg=BACKCOLOR,
                           font=FONT2, command=import_csv)
    import_button.grid(row=3, column=0)
    export_button = Button(app.menu_options_frame, text="Export", width=8, relief='flat', bg=FRONTCOLOR, fg=BACKCOLOR,
                           font=FONT2, command=export_csv)
    export_button.grid(row=4, column=0)
    group_button = Button(app.menu_options_frame, text="Groups", width=8, relief='flat', bg=FRONTCOLOR, fg=BACKCOLOR,
                          font=FONT2, command=group_form)
    group_button.grid(row=5, column=0)
    type_button = Button(app.menu_options_frame, text="Types", width=8, relief='flat', bg=FRONTCOLOR, fg=BACKCOLOR,
                         font=FONT2, command=type_form)
    type_button.grid(row=6, column=0)
    exit_button = Button(app.menu_options_frame, text="Exit", width=8, relief='flat', bg=FRONTCOLOR, fg=BACKCOLOR,
                         font=FONT2, command=exit_door)
    exit_button.grid(row=7, column=0)
    mt = mytree.TreeviewCreate(tree_frame)
    create_db()
    settinf.port_reader()
    firma = firmname()
    mt.frimlabel.config(text=firma)
    w.mainloop()


    # main_button.bind("<Enter>", on_enter_main)
    # main_button.bind("<Leave>", on_leave_main)
    # setting_button.bind("<Enter>", on_enter_frame)
    # setting_button.bind("<Leave>", on_leave_frame)
    # import_button.bind("<Enter>", on_enter_import)
    # import_button.bind("<Leave>", on_leave_import)
    # export_button.bind("<Enter>", on_enter_export)
    # export_button.bind("<Leave>", on_leave_export)
    # group_button.bind("<Enter>", on_enter_group)
    # group_button.bind("<Leave>", on_leave_group)
    # type_button.bind("<Enter>", on_enter_type)
    # type_button.bind("<Leave>", on_leave_type)
    # exit_button.bind("<Enter>", on_enter_exit)
    # exit_button.bind("<Leave>", on_leave_exit)



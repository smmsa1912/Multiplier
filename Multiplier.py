def main():
    def existing(data1_path):
        import wmi

        # Initializing the wmi constructor
        f = wmi.WMI()

        # Printing the header for the later columns
        file = open(data1_path, 'w+')
        file.truncate(0)
        # Iterating through all the running processes
        try:
            try:
                print('\nScanning And Writing Data1')
                for process in f.Win32_Process():
                    Names = f"{process.Name}\n"
                    file.write(Names)
                return True
            except:
                return False
        except FileNotFoundError:
            print(
                '\n\nAn Unexpected Error Occured While Writing Data1!! Look Like The Required Files Are Getting Deleted!!')
            print('Retrying!! :)')
            find(data1_path, data2_path, exe_path)

    # Gather All Executable Applications Path

    def fullscn(exe_path):
        import win32api
        import datetime

        date = datetime.date.today()
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')
        Next_Scan_Date = (datetime.date.today() +
                          datetime.timedelta(days=7)).strftime('%d-%m-%Y')
        Scanned_Date = '{}-{}-{}'.format(day, month, year)

        file = open(exe_path, 'w+')
        file.truncate(0)
        import os
        print('\nScanning And Writing Exe')
        print(
            'This Will Take A Few Minute!! -> (Depending On Number Of Applications You Have Installed In This Device!)')
        print('Kindly Wait :)')

        try:
            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split('\000')[:-1]
            drive = 0
            total_drives = len(drives)
            exe = open(exe_path, 'a+')
            exe.write('Scanned Date : {}, \t Next Scanning Date : {}\n'.format(
                Scanned_Date, Next_Scan_Date))
            exe.close()
            for Drives in drives:
                for root, dirs, files in os.walk(Drives):
                    for file in files:
                        if file.endswith(".exe"):
                            name = file.endswith(".exe")
                            Path = os.path.join(root, file)
                            Path = Path + '\n'
                            file = open(exe_path, 'a+')
                            file.write(Path)
                            # Line Counter
                            file = open(exe_path, "r")
                            Counter = 0
                            # Reading from file
                            Content = file.read()
                            CoList = Content.split("\n")

                            for i in CoList:
                                if i:
                                    Counter += 1
                            print('Number Of Executable Path Found :', str(
                                Counter)+',', 'Progress Done : ('+str(drive)+'/'+str(total_drives)+')', end='\r')
                drive += 1
            exe = open(exe_path, 'a+')
            exe.write('End Of List')
        except FileNotFoundError:
            print(
                '\nAn Unexpected Error Occured While Writing Exe File!! Look Like The Required Files Are Getting Deleted!!')
            print('Retrying!! :)')
            find(data1_path, data2_path, exe_path)
        print('Scanning And Writing Done Successfully!!, "Progress Done : (' +
              str(drive)+'/'+str(total_drives)+')"                                 ')

    # Gather Background Applications List List (2)

    def runner(data2_path):
        import wmi
        while True:
            # Initializing the wmi constructor
            f = wmi.WMI()

            # Printing the header for the later columns
            file = open(data2_path, 'w+')
            file.truncate(0)
            # Iterating through all the running processes
            try:
                try:
                    print('\nScanning And Writing Data2')
                    for process in f.Win32_Process():
                        Names = f"{process.Name}\n"
                        file.write(Names)
                    return True
                except:
                    return False
            except FileNotFoundError:
                print(
                    '\nAn Unexpected Error Occured While Writing Data2!! Look Like The Required Files Are Getting Deleted!!')
                print('Retrying!! :)')
                find(data1_path, data2_path, exe_path)

    blacklist = []
    opened = []
    closed = []

    # Compare Data1 And Data2

    def check(data1_path, data2_path):
        Data2 = open(data2_path, 'r')
        Data1 = open(data1_path, 'r')
        data1 = Data1.read()
        data2 = Data2.readlines()
        for Data in data2:
            print('\n')
            Dat = Data.replace('\n', '')
            print('Trying To Find :', Dat, 'In Data1')
            if Data in data1:
                print('Found :', Dat)
            else:
                print('Cant Find :', Dat)
                opened.append(Data)
                blacklist.append(Data)
    ''' Data1 = open(data1_path, 'w+')
        Data2 = open(data2_path, 'r')
        data = Data2.read()
        print('Editing Data1')
        Data1.write(data)
        print('Editing Data1 Done!!')'''

    # Compare Data2 And Data1

    def Check(data1_path, data2_path):
        data1 = open(data1_path, 'r')
        data2 = open(data2_path, 'r')
        data1 = data1.readlines()
        data2 = data2.read()

        for data in data1:
            print('\n')
            Dat = data.replace('\n', '')
            print('Trying To Find :', Dat, 'In Data2')
            if data in data2:
                print('Found', Dat, 'In Data2')
            else:
                print('Cant Find :', data)
                closed.append(data)
                blacklist.append(data)
        Data1 = open(data1_path, 'w+')
        Data2 = open(data2_path, 'r')
        data = Data2.read()
        print('Editing Data1')
        Data1.write(data)
        print('Editing Data1 Done!!')

    # Run Application Of Given Path

    def start(path, names):
        i = 0
        brk_num = 3
        import os
        print('Trying To Execute :', names)
        while True:
            def start_app(path):
                try:
                    os.startfile(path)
                except:
                    return False
            if start_app(path) is False:
                name = names.replace('\n', '')
                print('Cant Execute :', name, ':(')
                return False
            else:
                name = names.replace('\n', '')
                print('Executed successfully :', name, ':)')
                i += 1

            if i == brk_num:
                for list in blacklist:
                    if names in list:
                        index = blacklist.index(names)
                        print('Removing :', names)
                        try:
                            blacklist.pop(int(index))
                        except:
                            print('Cant Remove :', name)
                    else:
                        break
            if i == brk_num:
                break

        if i == brk_num:
            i = 0
            return True

    # Gather Path And List Of Application To Start File

    def starter(exe_path):
        print('List Of Applications :', blacklist)
        while bool(blacklist):
            lists = blacklist
            if len(lists) != 0 and bool(blacklist) is True:
                rst = None
                file = open(exe_path, 'r')
                for names in lists:
                    for path in file:
                        if path.endswith(names):
                            print('Executble Path Found For :', names)
                            if '\n' in path:
                                path = path.replace('\n', '')
                            if '\n' in lists:
                                names = names.replace('\n', '')
                            rst = start(path, names)
                        elif path == 'End Of List' and rst is True or False:
                            starter(exe_path)
                        elif path == 'End Of List' and rst is None:
                            print('Cant Find Path Of Application :', names)
                            for list in blacklist:
                                if names in list:
                                    index = blacklist.index(names)
                                    print('Removing :', names)
                                    blacklist.pop(int(index))
                            print('Rechecking List')
                            starter(exe_path)

            else:
                print('No Executable Application Found..!!')
                break

    def Installed_Apps(application_path):
        Last_scanned = 0
        Applications = open(application_path, 'r')
        Applications = Applications.read()
        if 'Total Installed Applications : ' in Applications:
            Applications = open(application_path, 'r')
            last_line = Applications.readlines()[-1]
            last_line = last_line.split(',')[:1]
            last_line = ''.join(last_line).split(':')[1:]
            last_line = ''.join(last_line).replace(' ', '')
            Last_scanned = last_line
        Applications = open(application_path, 'w+')
        Applications.truncate(0)
        Applications = open(application_path, 'a+')
        import winapps
        # get each application with list_installed()
        Installed_Apps = 0
        for item in winapps.list_installed():
            Applications.write(str(item.name)+'\n')
            if item:
                Installed_Apps += 1
        Applications.write(
            'Total Installed Applications : '+str(Installed_Apps)+', Previously Scanned Result : '+str(Last_scanned))
        Applications.close()

    def find(data1_path, data2_path, exe_path, application_path):
        tried = 0
        import os
        while True:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            newpath = dir_path + '\Content'
            if not os.path.exists(newpath):
                print('\nCant Find The Directory')
                print('Creating A Directory..!!', end='\r')
                os.makedirs(newpath)
                print('Creating A Directory Done Successfully..!!')

            if tried != 0:
                print('Rechecking For Required Files')

            list = ['Data1', 'Data2', 'Exe', 'Application']
            # This is to get the directory that the program
            # is currently running in.
            Data1 = False
            Data2 = False
            Exe = False
            Applications = False
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    for names in list:
                        if file.endswith(names):
                            # print(root+'\\'+str(file))
                            if names == 'Data1':
                                Data1 = True
                            if names == 'Data2':
                                Data2 = True
                            if names == 'Exe':
                                Exe = True
                            if names == 'Application':
                                Applications = True
            if Data1 is True and Data2 is True and Exe is True and Applications is True:
                if tried != 0:
                    print('All Required Files Found!!')
                return True
            else:
                if Data1 is False:
                    print('Cant Find Data1')
                    existing(data1_path)
                if Data2 is False:
                    print('Cant Find Data2')
                    runner(data2_path)
                if Exe is False:
                    print('Cant Find Exe')
                    fullscn(exe_path)
                if Applications is False:
                    print('Cant Find Application')
                    Installed_Apps(application_path)
            tried += 1

    def path(dir_of):
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.dirname(os.path.abspath(__file__))
        newpath = dir_path + '\Content'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        result = None
        data1_path = None
        data2_path = None
        exe_path = None
        application_path = None
        lists = ['Data1', 'Data2', 'Exe', 'Application']
        for root, dirs, files in os.walk(path):
            for name in lists:
                if name in files:
                    result = os.path.join(root, name)
                    if name == 'Data1':
                        data1_path = result
                    if name == 'Data2':
                        data2_path = result
                    if name == 'Exe':
                        exe_path = result
                    if name == 'Application':
                        application_path = result
        if data1_path is None:
            data1_path = path + '\Content\Data1'
        else:
            pass
        if data2_path is None:
            data2_path = path + '\Content\Data2'
        else:
            pass
        if exe_path is None:
            exe_path = path + '\Content\Exe'
        else:
            pass
        if application_path is None:
            application_path = path + '\Content\Application'
        else:
            pass

        if dir_of == 'Data1':
            return data1_path
        if dir_of == 'Data2':
            return data2_path
        if dir_of == 'Exe':
            return exe_path
        if dir_of == 'Application':
            return application_path

    data1_path = path('Data1')
    data2_path = path('Data2')
    exe_path = path('Exe')
    application_path = path('Application')
    # Main
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path + '\Content'):
        p = os.popen('attrib -h ' + dir_path + '\Content')
    if existing(data1_path):
        print('Scanning And Writing Done Successfully..!!')
        if runner(data2_path):
            print('Scanning And Writing Done Successfully..!!')
            while True:
                if os.path.exists(dir_path + '\Content'):
                    p = os.popen('attrib -h ' + dir_path + '\Content')
                Installed_Apps(application_path)
                if os.path.exists(application_path):
                    app = open(application_path, 'r')
                    app = app.read()
                    if 'Total Installed Applications :' not in app:
                        Installed_Apps(application_path)
                    if 'Total Installed Applications :' in app:
                        Previous_Scan = 0
                        Current_Scan = 0
                        Applications = open(application_path, 'r')
                        last_line = Applications.readlines()[-1]
                        last_line = last_line.split(',')[1:]
                        last_line = ''.join(last_line).split(':')[1:]
                        Previous_Scan = ''.join(last_line).replace(' ', '')

                        Applications = open(application_path, 'r')
                        last_line = Applications.readlines()[-1]
                        last_line = last_line.split(',')[:1]
                        last_line = ''.join(last_line).split(':')[1:]
                        Current_Scan = ''.join(last_line).replace(' ', '')
                        if Previous_Scan == Current_Scan:
                            pass
                        else:
                            if Previous_Scan < Current_Scan:
                                print(
                                    'Look Like A You Have Installed A New Application! Resccanning Datas')
                                fullscn(exe_path)
                            elif Previous_Scan > Current_Scan:
                                print(
                                    'Look Like A You Have Uninstalled A Application! Resccanning Datas')
                                fullscn(exe_path)
                if os.path.exists(exe_path):
                    import datetime
                    exe = open(exe_path, 'r')
                    ex = exe.readlines(1)
                    a = str(ex).split(',')
                    Next_Scan_Date = str(str(a[1:]).split(':')[1:]).replace('\\', '').replace(
                        ']', '').replace('[', '').replace('"', '').replace("'", '').replace('n', '').replace(' ', '')

                    date = datetime.date.today()
                    year = date.strftime('%Y')
                    month = date.strftime('%m')
                    day = date.strftime('%d')
                    Scanned_Date = '{}-{}-{}'.format(day, month, year)

                    if 'End Of List' not in exe:
                        print('\nLook Like Exe File Does Not Scanned Fully!!')
                        print('Kindly Let The Scanning Done Completely!!')
                        print('Rescanning Exe File!!')
                        fullscn(exe_path)
                    if Next_Scan_Date <= Scanned_Date:
                        print('\nLast Scanned Exe File Has Been Expired!!')
                        print('Scanning Exe File Again! ')
                        fullscn(exe_path)
                if find(data1_path, data2_path, exe_path, application_path) is True:
                    import os
                    c_exe = os.stat(exe_path).st_size == 0
                    if c_exe:
                        print('Look Like There Is Nothing In Exe File')
                        fullscn(exe_path)
                    c_Data1 = os.stat(data1_path).st_size == 0
                    if c_Data1:
                        print('Look Like There Is Nothing In Data1 File')
                        existing(data1_path)
                    Apps = os.stat(application_path).st_size == 0
                    if Apps:
                        print('Look Like There Is Nothing In Applications File')
                        Installed_Apps(application_path)

                    Data1 = open(data1_path, 'r')
                    Data2 = open(data2_path, 'r')
                    Data1 = Data1.read()

                    with open(data1_path, 'r') as fp:
                        for count, line in enumerate(fp):
                            pass
                        # print('\nNumber Of Line In Data1:', count + 1)
                        c_Data1 = count + 1
                    with open(data2_path, 'r') as fp:
                        for count, line in enumerate(fp):
                            pass
                        # print('Number Of Line In Data2:', count + 1)
                        c_Data2 = count + 1
                    if c_Data1 != c_Data2:
                        blacklist.clear()
                        check(data1_path, data2_path)
                        Check(data1_path, data2_path)
                        starter(exe_path)
                        print('All Done Rescanning....')
                        runner(data2_path)

                    else:
                        print('No Changes Detected..!!\nRescanning!!')
                        runner(data2_path)
                else:
                    import os
                    print('All Unexpected Error Occured..!!')
                    if os.path.exists(dir_path + '\Content'):
                        p = os.popen('attrib +h ' + dir_path + '\Content')
                        exit()


def exit():
    a = input('Kindly Press Enter To Quit..!!')
    if a == '':
        quit()
    else:
        exit()


try:
    print('Created By SMMSA :)')
    main()
except KeyboardInterrupt:
    import os
    print('\nAn Error Occured While Running Main File..!! :(')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path + '\Content'):
        p = os.popen('attrib +h ' + dir_path + '\Content')
    exit()
except PermissionError:
    print('\nAn Unexpected Permission Error Occured!! Try Running As Administrator :)')
    exit()
except FileNotFoundError:
    print('Retrying!!')
    main()
except Exception as e:
    repet = 0
    import os
    import time
    print(e)
    print('\nAn Error Occured While Running Main File..!! :(')
    print('Retrying To Run Main File In 3 Second..!!')
    time.sleep(3)
    main()
    repet += 1
    if repet == 1:

        dir_path = os.path.dirname(os.path.realpath(__file__))
        if os.path.exists(dir_path + '\Content'):
            p = os.popen('attrib +h ' + dir_path + '\Content')
        exit()
except:
    print('Look like Something Went Wrong!! :(\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path + '\Content'):
        p = os.popen('attrib +h ' + dir_path + '\Content')
    exit()

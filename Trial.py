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
            print('\nScanning And Writing Data1')
            for process in f.Win32_Process():
                Names = f"{process.Name}\n"
                file.write(Names)
            return True
        except:
            return False
    # Gather All Executable Applications Path

    def fullscn(exe_path):
        file = open(exe_path, 'w+')
        file.truncate(0)
        import os
        print('\nScanning And Writing Exe')
        print('This Will Take A Few Minute!! -> (Depending On How Many Applications You Have Installed In Your Device!)')
        print('Kindly Wait :)')
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                if file.endswith(".exe"):
                    name = file.endswith(".exe")
                    Path = os.path.join(root, file)
                    Path = Path+'\n'
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
                    print('Number Of Line Written :', Counter, end='\r')
        exe = open(exe_path, 'a+')
        exe.write('End Of List')
        print('Scanning And Writing Done Successfully!!')

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
                print('\nScanning And Writing Data2')
                for process in f.Win32_Process():
                    Names = f"{process.Name}\n"
                    file.write(Names)
                return True
            except:
                return False

    blacklist = []

    # Compare Data1 And Data2

    def check(data1_path, data2_path):
        Data2 = open(data2_path, 'r')
        Data1 = open(data1_path, 'r')
        data1 = Data1.read()
        for Data in Data2:
            print('Trying To Find :', Data)
            if Data in data1:
                print('Found :', Data)
            else:
                print('Cant Find :', Data)
                blacklist.append(Data)
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
        print('Starting :', names)
        while True:
            def start_app(path):
                try:
                    os.startfile(path)
                except:
                    return False

            if start_app(path) is False:
                print(names, ': Cant Start')
                return False
            else:
                print(names, ': Started successfully!')
                i += 1

            if i == brk_num:
                for list in blacklist:
                    if names in list:
                        index = blacklist.index(names)
                        print('Removing :', names)
                        blacklist.pop(int(index))
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
                            print('Executble Path Found!')
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

    def find(data1_path, data2_path, exe_path):
        tried = 0
        import os
        while True:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            newpath = dir_path+'\Content'
            if not os.path.exists(newpath):
                print('\nCant Find The Directory')
                print('Creating A Directory..!!', end='\r')
                os.makedirs(newpath)
                print('Creating A Directory Done Successfully..!!')

            if tried != 0:
                print('Rechecking For Required Files')

            list = ['Data1', 'Data2', 'Exe']
            # This is to get the directory that the program
            # is currently running in.
            Data1 = False
            Data2 = False
            Exe = False
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
            if Data1 is True and Data2 is True and Exe is True:
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
            tried += 1

    def path(dir_of):
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.dirname(os.path.abspath(__file__))
        newpath = dir_path+'\Content'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        result = None
        data1_path = None
        data2_path = None
        exe_path = None
        lists = ['Data1', 'Data2', 'Exe']
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
        if data1_path is None:
            data1_path = path+'\Content\Data1'
        else:
            data1_path
        if data2_path is None:
            data2_path = path+'\Content\Data2'
        else:
            data2_path
        if exe_path is None:
            exe_path = path+'\Content\Exe'
        else:
            exe_path

        if dir_of == 'Data1':
            return data1_path
        if dir_of == 'Data2':
            return data2_path
        if dir_of == 'Exe':
            return exe_path

    data1_path = path('Data1')
    data2_path = path('Data2')
    exe_path = path('Exe')

    # Main
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path+'\Content'):
        p = os.popen('attrib -h ' + dir_path+'\Content')
    if existing(data1_path):
        print('Scanning And Writing Done Successfully..!!')
        if runner(data2_path):
            print('Scanning And Writing Done Successfully..!!')
            while True:
                if os.path.exists(dir_path+'\Content'):
                    p = os.popen('attrib -h ' + dir_path+'\Content')
                if find(data1_path, data2_path, exe_path) is True:
                    import os
                    c_exe = os.stat(exe_path).st_size == 0
                    if c_exe:
                        print('Look Like There Is Nothing In Exe File')
                        fullscn(exe_path)
                    c_Data1 = os.stat(data1_path).st_size == 0
                    if c_Data1:
                        print('Look Like There Is Nothing In Data1 File')
                        existing(data1_path)

                    Data1 = open(data1_path, 'r')
                    Data2 = open(data2_path, 'r')
                    Data1 = Data1.read()

                    with open(data1_path, 'r') as fp:
                        for count, line in enumerate(fp):
                            pass
                        print('\nNumber Of Line In Data1:', count + 1)
                        c_Data1 = count + 1
                    with open(data2_path, 'r') as fp:
                        for count, line in enumerate(fp):
                            pass
                        print('Number Of Line In Data2:', count + 1)
                        c_Data2 = count + 1
                    if c_Data1 != c_Data2:
                        blacklist.clear()
                        check(data1_path, data2_path)
                        starter(exe_path)
                        print('All Done Rescanning....')
                        runner(data2_path)

                    else:
                        print('No Changes Detected..!!\nRescanning!!')
                        runner(data2_path)
                else:
                    import os
                    print('All Unexpected Error Occured..!!')
                    if os.path.exists(dir_path+'\Content'):
                        p = os.popen('attrib +h ' + dir_path+'\Content')
                        exit()


def exit():
    a = input('Kindly Press Enter To Quit..!!')
    if a == '':
        quit()
    else:
        exit()


try:
    main()
except KeyboardInterrupt:
    import os
    print('\nAn Error Occured While Running Main File..!! :(')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path+'\Content'):
        p = os.popen('attrib +h ' + dir_path+'\Content')
    exit()
except Exception as e:
    repet = 0
    print(e)
    import os
    import time
    print('\nAn Error Occured While Running Main File..!! :(')
    print('Retrying To Run Main File In 3 Second..!!')
    time.sleep(3)
    main()
    repet += 1
    if repet == 1:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if os.path.exists(dir_path+'\Content'):
            p = os.popen('attrib +h ' + dir_path+'\Content')
        exit()

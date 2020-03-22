#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# SMcElmurry, 2020Mar21,   Added code to handle track information under menu option "c" (see TODone)
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

#lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstFileNames = ['TestCD.txt', 'TestTrack.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = IO.ScreenIO.value_Errors(int, "Select the CD / Album index: ", "Choice must match existing indices! ")
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODone add code to handle tracks on an individual CD
        IO.ScreenIO.print_CD_menu()
        cd_choice = ""
        while True:
            cd_choice = IO.ScreenIO.menu_CD_choice()
            if cd_choice == "x":
                break
            elif cd_choice == "d":
                print(cd.get_long_record())
            elif cd_choice == "a":
                tkID, tkTitle, tkLen = IO.ScreenIO.get_track_info()
                new_track = (tkID, tkTitle, tkLen)
                PC.DataProcessor.add_track(new_track, cd)
            elif cd_choice == "r":
                IO.ScreenIO.show_tracks(cd)
                trk_choice = IO.ScreenIO.value_Errors(int, "What track would you like to remove?: ", "Choice must match existing indices! ")
                cd.rmv_track(trk_choice)
            else:
                print("General Error")
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')
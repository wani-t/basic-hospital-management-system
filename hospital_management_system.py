import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    print("\n------- Hospital Management System -------\n")
    print("1. Create/Import New Dataframe")
    print("2. Patient Data Analysis")
    print("3. Patient Data Visualisation")
    print("4. Export Dataframe to csv file")
    
def create_dataframe_menu():
    print("\n------- Create Dataframe -------\n")
    print("1. Create Dataframe")
    print("2. Import Dataframe from csv file")
    print("3. Add/Modify Custom Index")
    print("4. Add/Modify Custom Column Head")

def analysis_menu():
    print("\n------- Data Analysis using Python -------\n")
    print("1. Display All records")
    print("2. Print first nth records.")
    print("3. Print last nth records.")
    print("4. Print patient records in alphabetical order.")
    print("5. Display inpatient surgery records.")
    print("6. Display outpatient surgery records.")
    print("7. Display records of patients discharged.")
    print("8. Print distinct surgery type.")
    print("9. Add another entry to Dataframe.")
    print("10. Delete an entry from Dataframe.")
    print("11. Return to main menu.")
    
def visualisation_menu():
    print("\n------- Visualisation using Matplotlib -------\n")
    print("1. Plot Line graph (No. of patients per surgery type)")
    print("2. Plot Line graph (No. of patients per blood group type)")
    print("3. Plot Line graph (No. of patients per Surgeon)")
    print("4. Return to main menu.")
cols =
['patient_id','name','dob','blood_group','surgery_type','surgeon','discharge_status','patient_type']
 
df = pd.DataFrame([],columns = cols) # Create an EmptyDataFrame

while True:
    main_menu()
    ch = int(input("Select Option: "))
    if ch == 1:
        # Create New Dataframe
        create_dataframe_menu()
        ch = int(input("Select Option: "))
    if ch == 1:
        data = []
        while True:
            ch = input("Add Row [y/n]")
            if ch.lower() == 'y':
                patient_id = input("Patient ID: ")
                name = input("Patient Name: ")
                dob = input("DOB in dd-mm-yyyy format: ")
                blood_group = input("Blood Group: ")
                surgery_type = input("Surgery type: ")
                surgeon = input("Name of Surgeon (please enter name in block letters): ")
                discharge_status = input("Discharge status y/n: ")
                patient_type = input("inpatient/outpatient: ")
                data.append([patient_id, name, dob, blood_group, surgery_type, surgeon, discharge_status, patient_type])
            else:
                break
    df = pd.DataFrame(data, columns = cols)

    elif ch == 2:
        file = input("File name: ") #File should be saved in csv format. File path to be pasted without quotes.
        df = pd.read_csv(file)
        print(df)
    elif ch == 3:
        index_list = input("Index List: ").split(",")
        df.index = index_list
    elif ch == 4:
        column_list= input("Column List: ").split(",")
        df.columns = column_list
        print(df)

elif ch == 2:
     while True:
         # Patient Data Analysis
         analysis_menu()
         ch = int(input("Select Option: "))
         if ch == 1:
             print(df)
         elif ch == 2:
             nth = int(input("Enter no of rows to display: "))
             print(df.head(nth))
         elif ch == 3:
             nth = int(input("Enter number of rows to display: "))
             print(df.tail(nth))
         elif ch == 4:
             print(df.sort_values(by='name'))
         elif ch == 5:
             print(df[df['patient_type'] == 'inpatient'])
         elif ch == 6:
             print(df[df['patient_type'] == 'outpatient'])
         elif ch == 7:
             print(df[df['discharge_status'] == 'y'])
         elif ch == 8:
             print(df['surgery_type'].unique())
         elif ch == 9:
             while True:
                 ch = input("Add Row [y/n]")
                 if ch.lower() == 'y':
                     patient_id = input("Patient ID: ")
                     name = input("Patient Name: ")
                     dob = input("DOB in dd-mm-yyyy format: ")
                     blood_group = input("Blood Group: ")
                     surgery_type = input("Surgery type: ")
                     surgeon = input("Name of Surgeon: ")
                     discharge_status = input("y/n: ")
                     patient_type = input("inpatient/outpatient: ")
                     data.append([patient_id, name, dob, blood_group, surgery_type, surgeon, discharge_status, patient_type])
                 else:
                     break
         elif ch == 10:
             print("1. Delete Row by Index")
             print("2. Delete Row by Patient ID.")
             ch = int(input("Select Option: "))
             if ch == 1:
                 idx = int(input("Index to delete: "))
                 df = df.drop(index = idx)
             elif ch == 2:
                 ptid = int(input("Patient ID no. to delete: "))
                 df = df.drop(df[df["patient_id"] == ptid].index)
             else:
                 print("Please enter valid option.")
        else:
            print("Returning to main menu")
            break


elif ch == 3:
    while True:
        # Patient Data Visualisation
        visualisation_menu()
        ch = int(input("Select Option: "))
    if ch == 1:
        p = df.surgery_type.unique()
        p_list = list(p)
        z = df.groupby('surgery_type').count()
        z_list = z.values.tolist()
        plt.plot(p_list,z_list, color='blue')
        plt.xlabel("Surgery Type", fontsize=12)
        plt.ylabel("No. of patient", fontsize=12)
        plt.title("Patient - Surgery type Visualisation", fontsize=14)
        plt.show()
        
    elif ch == 2:
        x = df.blood_group.unique()
        x_values = list(x)
        y = df.groupby('blood_group').count()
        y_values = y.values.tolist()
        plt.plot(x_values, y_values, color = 'black')
        plt.xlabel("Blood type", fontsize=12)
        plt.ylabel("No. of patients", fontsize=12)
        plt.title("Patient - Blood type Visualisation", fontsize=14)
        plt.show()

    elif ch == 3:
        a = df.surgeon.unique()
        a_values = list(a)
        b = df.groupby('surgeon').count()
        b_values = b.values.tolist()
        plt.plot(a_values, b_values, color = 'magenta')
        plt.xlabel("Surgeon Name", fontsize=12)
        plt.ylabel("No. of patients", fontsize=12)
        plt.title("Data visualisation of No. of patients per Surgeon", fontsize=14)
        plt.show()
    elif ch == 4:
        print("Returning to main menu.")
        break
    else:
        print("OPTION INVALID ")

elif ch == 4:
    # Export Dataframe to csv file
    file = input("File name: ")
    df.to_csv(file, index = False)
    
elif ch == 5:
    # Exit
    print("exiting")
    exit()
    
else:
    # Error Display and Exit
    print("INVALID OPTION")
    break

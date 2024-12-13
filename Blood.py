def generate_blood_report():
    print("Welcome to the Blood Report Generator!")
    print("-------------------------------------")
    
    # Input from the user
    name = input("Enter the patient's name: ")
    age = int(input("Enter the patient's age: "))
    gender = input("Enter the patient's gender (M/F): ")
    
    # Collect blood test results
    print("\nEnter the following test results:")
    hemoglobin = float(input("Hemoglobin (g/dL): "))
    wbc_count = float(input("White Blood Cell Count (10^9/L): "))
    platelet_count = float(input("Platelet Count (10^9/L): "))
    rbc_count = float(input("Red Blood Cell Count (million/µL): "))
    
    # Reference ranges
    ref_ranges = {
        "hemoglobin": (13.8, 17.2) if gender.upper() == "M" else (12.1, 15.1),
        "wbc_count": (4.0, 11.0),
        "platelet_count": (150, 450),
        "rbc_count": (4.7, 6.1) if gender.upper() == "M" else (4.2, 5.4)
    }
    
    # Evaluate test results
    print("\nBlood Report:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print("-------------------------------------")
    
    def check_range(value, ref_range):
        return "Normal" if ref_range[0] <= value <= ref_range[1] else "Abnormal"
    
    # Display results
    print(f"Hemoglobin: {hemoglobin} g/dL ({check_range(hemoglobin, ref_ranges['hemoglobin'])})")
    print(f"WBC Count: {wbc_count} x10^9/L ({check_range(wbc_count, ref_ranges['wbc_count'])})")
    print(f"Platelet Count: {platelet_count} x10^9/L ({check_range(platelet_count, ref_ranges['platelet_count'])})")
    print(f"RBC Count: {rbc_count} million/µL ({check_range(rbc_count, ref_ranges['rbc_count'])})")
    print("-------------------------------------")
    print("Note: Consult your doctor for a detailed analysis of your results.")
    

generate_blood_report()
def search_patients(patients, disease):
    return [p["Name"] for p in patients if p["Disease"] == disease]

n = int(input("Enter number of patients: "))
patients = []
for _ in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
search_disease = input("Enter disease to search: ")
print("Patients with", search_disease + ":", search_patients(patients, search_disease))

#hopspital_python



class Patient(object):

    patient_count = 0

    def __init__(self, name, allergies):

        self.name = name

        self.allergies = allergies

        self.id = Patient.patient_count

        self.bed_number = None

        Patient.patient_count += 1



class Hospital(object):

    def __init__(self,name,cap):

        self.name = name

        self.capacity = capacity

        self.patients = []

        self.bed = self.initialize_bed()



    def initialize_bed(self):

        beds = []

        for i in range(0,self.cap):

            beds.append({

                "bed_id": i,

                "Available": True

            })

        return beds

    

    def admit(self,patient):

        if len(self.patients) <= self.capacity:

            self.patients.append(patient)

            for i in range(0, len(self.beds)):

                if self.beds[i]["Available"]:

                    patient.bed_number = self.beds[i]["bed_id"]

                    self.beds[i]["Available"] = False

                    break

            print "Patient #{} admitted to bed #{}".format(patient.id, patient. bed_number)

        else:

            "Hospital is at full capacity"

    def discharge(self,patient_id):

        for patient in self.patients:

            if patient.id == patient_id:

                for bed in self.beds:

                    if bed["bed_id"] == patient.bed_number:

                        bed["Available"] = True

                        break



                self.patients.remove(patient)

                return "Patient #{} has been discharged. Bed #{} is now available.".format(patient.id, patient.bed_number)

        return "Patient not found"



Tim = Patient("Tim", "Jerks")

patientadmit = Hospital().admit(Tim).initialize_bed().discharge()
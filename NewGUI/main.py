import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QGridLayout, QPushButton, QCheckBox, QGroupBox

app = QApplication(sys.argv)
root = QWidget()


#Default Sizes
defaultInputWidth = 200
defaultInputHeight = 25

# Layouts
root_layout = QVBoxLayout(root)
top_frame_layout = QHBoxLayout()
insurance_frame_layout = QVBoxLayout()
patient_frame_layout = QVBoxLayout()
doctor_frame_layout = QVBoxLayout()
items_frame_layout = QVBoxLayout()
diagnosis_frame_layout = QVBoxLayout()
submit_frame_layout = QVBoxLayout()

# Insurance Frame
insurance_frame = QGroupBox("Insurance")
insurance_frame.setLayout(insurance_frame_layout)
insurance_list = QComboBox()
insurance_list.addItems(["IEHP", "Medicare"])
insurance_list.setFixedSize(100,25)
insurance_frame_layout.addWidget(QLabel("User Name"))
insurance_frame_layout.addWidget(QLineEdit())
insurance_frame_layout.addWidget(insurance_list)


# Patient Frame
patient_frame = QGroupBox("Patient")
patient_grid_layout = QGridLayout()  # Change this line
patient_frame.setLayout(patient_grid_layout)

patient_labels = [
    QLabel("First Name"),
    QLabel("Last Name"),
    QLabel("Street"),
    QLabel("City"),
    QLabel("Zip"),
    QLabel("State"),
    QLabel("Phone Number"),
    QLabel("Date Of Service"),
    QLabel("Date Of Birth"),
    QLabel("Insurance ID"),
    QLabel("Pre-auth"),
]

patient_inputs = [QLineEdit() for _ in range(len(patient_labels))]

# Add labels and input widgets to the patient_grid_layout
rows = 2
cols = len(patient_labels) // rows
for i, (label, input_widget) in enumerate(zip(patient_labels, patient_inputs)):
    row, col = divmod(i, cols)
    patient_grid_layout.addWidget(label, row, col * 2)
    patient_grid_layout.addWidget(input_widget, row, col * 2 + 1)

# Doctor Frame
doctor_frame = QGroupBox("Doctor")
doctor_frame.setLayout(doctor_frame_layout)
doctor_frame_layout.addWidget(QLabel("First Name"))
doctor_frame_layout.addWidget(QLineEdit())
doctor_frame_layout.addWidget(QLabel("Last Name"))
doctor_frame_layout.addWidget(QLineEdit())
doctor_frame_layout.addWidget(QLabel("Street"))
doctor_frame_layout.addWidget(QLineEdit())
doctor_frame_layout.addWidget(QLabel("State"))
doctor_frame_layout.addWidget(QLineEdit())
doctor_frame_layout.addWidget(QLabel("Zip"))
doctor_frame_layout.addWidget(QLineEdit())
doctor_frame_layout.addWidget(QLabel("NPI"))
doctor_frame_layout.addWidget(QLineEdit())
search_npi_button = QPushButton("Search NPI")
doctor_frame_layout.addWidget(search_npi_button)

# Items Frame
items_frame = QGroupBox("Items")
items_frame.setLayout(items_frame_layout)
grid_layout = QGridLayout()
items_frame_layout.addLayout(grid_layout)

for i in range(6):
    for j in range(7):
        grid_layout.addWidget(QLineEdit(), i, j)

# Diagnosis Frame
diagnosis_frame = QGroupBox("Diagnosis")
diagnosis_frame.setLayout(diagnosis_frame_layout)
diagnosis_frame_layout.addWidget(QLabel("Diagnosis Code"))
diagnosis_frame_layout.addWidget(QLineEdit())
diagnosis_frame_layout.addWidget(QLabel("Diagnosis Description"))
diagnosis_frame_layout.addWidget(QLineEdit())

# Add patient and doctor frames to the top_frame_layout
top_frame_layout.addWidget(patient_frame)
top_frame_layout.addWidget(doctor_frame)

# Submit Frame
submit_frame = QGroupBox("Submit")
submit_frame.setLayout(submit_frame_layout)
submit_button = QPushButton("Submit")
submit_frame_layout.addWidget(submit_button)

# Add frames to root layout
root_layout.addWidget(insurance_frame)
root_layout.addLayout(top_frame_layout)
root_layout.addWidget(items_frame)
root_layout.addWidget(diagnosis_frame)
root_layout.addWidget(submit_frame)

root.show()
sys.exit(app.exec_())
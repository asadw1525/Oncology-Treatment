import pydicom
from django.shortcuts import render

def perform_analysis(dicom_data, pathology_report):
    
    patient_name = dicom_data.PatientName if hasattr(dicom_data, 'PatientName') else "Unknown"
    

    return f"Analysis completed for {patient_name}. Pathology report: {pathology_report[:50]}..."

def analyze_patient(request):
    if request.method == 'POST':
        pathology_report = request.POST.get('pathology_report')
        radiology_image = request.FILES.get('radiology_image')

        
        dicom_data = pydicom.dcmread(radiology_image)

       
        analysis_result = perform_analysis(dicom_data, pathology_report)

        return render(request, 'analyze_patient.html', {'analysis_result': analysis_result})

    return render(request, 'analyze_patient.html')

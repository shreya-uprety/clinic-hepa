from gcs_manager import GCSManager

gcs = GCSManager()
pid = "P_TEST"
prefix = f"patient_data/{pid}"

test_data = {"test": True, "items": [1, 2, 3]}

result = gcs.write_file(f"{prefix}/transcript.json", test_data)
print(f"Upload result: {result}")
print("Check: gs://clinic_sim/patient_data/P_TEST/transcript.json")

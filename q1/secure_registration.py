# PSHS Secure Club Registration System

def main():
    print("=== PSHS Secure Club Registration System ===\n")
    
    # 1. Student Name Validation (Must not be blank)
    student_name = input("Enter Student Name: ").strip()
    if not student_name:
        print("Error: Student name is required.")
        return
        
    # 2. Section Validation (Must match allowed section list)
    allowed_sections = [
        "Diamond", "Emerald", "Jade", "Sapphire", 
        "Dahlia", "Ilang-Ilang", "Rosal", "Sampaguita", 
        "Beryllium", "Magnesium", "Platinum", "Silicon", 
        "Electron", "Gluon", "Graviton", "Photon", 
        "Biology", "Chemistry", "Physics", "Bio-Chemistry"
    ]
    section = input("Enter Section: ").strip()
    matched_section = next((s for s in allowed_sections if s.lower() == section.lower()), None)
    if not matched_section:
        print("Error: Invalid section.")
        return
        
    # 3. Club Choice Validation (Must be from allowed list)
    allowed_clubs = ["Robotics", "Science", "Mathematics", "Programming"]
    club_choice = input("Enter Club Choice (Robotics, Science, Mathematics, Programming): ").strip()
    matched_club = next((c for c in allowed_clubs if c.lower() == club_choice.lower()), None)
    if not matched_club:
        print("Error: Please choose a valid club.")
        return
        
    # 4. School Email Validation (Must contain @ and .)
    school_email = input("Enter School Email: ").strip()
    if "@" not in school_email or "." not in school_email:
        print("Error: Invalid email format. Must contain @ and .")
        return
        
    # 5. Attendance Status Validation (Must be Present, Absent, or Late)
    allowed_attendance = ["Present", "Absent", "Late"]
    attendance_status = input("Enter Attendance Status (Present, Absent, Late): ").strip()
    matched_attendance = next((a for a in allowed_attendance if a.lower() == attendance_status.lower()), None)
    if not matched_attendance:
        print("Error: Invalid attendance status.")
        return
        
    # Success Output
    print("\n-----------------------------------")
    print("REGISTRATION ACCEPTED")
    print("-----------------------------------")
    print(f"Student: {student_name}")
    print(f"Section: {matched_section}")
    print(f"Club: {matched_club}")
    print(f"Email: {school_email}")
    print(f"Attendance: {matched_attendance}")
    print("-----------------------------------")

if __name__ == "__main__":
    main()

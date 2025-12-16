# appointment_service.py
# Task 1: Backend Service Implementation
# Simulates AppSync GraphQL + Aurora PostgreSQL

appointments = [
    {
        "id": 1,
        "name": "Azra Aysha",
        "date": "2025-09-20",
        "time": "10:00",
        "duration": 30,
        "doctorName": "Dr. John",
        "status": "Confirmed",
        "mode": "Online"
    },
    {
        "id": 2,
        "name": "Emily Rodriguez",
        "date": "2025-09-20",
        "time": "11:00",
        "duration": 20,
        "doctorName": "Dr. Smith",
        "status": "Upcoming",
        "mode": "Offline"
    },
    {
        "id": 3,
        "name": "Michael Chen",
        "date": "2025-09-19",
        "time": "09:30",
        "duration": 25,
        "doctorName": "Dr. Patel",
        "status": "Cancelled",
        "mode": "Online"
    },
    {
        "id": 4,
        "name": "Sarah Johnson",
        "date": "2025-09-18",
        "time": "14:00",
        "duration": 40,
        "doctorName": "Dr. Adams",
        "status": "Confirmed",
        "mode": "Offline"
    },
    {
        "id": 5,
        "name": "David Lee",
        "date": "2025-09-20",
        "time": "15:00",
        "duration": 30,
        "doctorName": "Dr. John",
        "status": "Upcoming",
        "mode": "Online"
    },
    {
        "id": 6,
        "name": "Aisha Khan",
        "date": "2025-09-17",
        "time": "12:00",
        "duration": 20,
        "doctorName": "Dr. Smith",
        "status": "Completed",
        "mode": "Offline"
    },
    {
        "id": 7,
        "name": "Rahul Mehta",
        "date": "2025-09-16",
        "time": "10:30",
        "duration": 30,
        "doctorName": "Dr. Patel",
        "status": "Completed",
        "mode": "Online"
    },
    {
        "id": 8,
        "name": "Sofia Martinez",
        "date": "2025-09-20",
        "time": "16:00",
        "duration": 35,
        "doctorName": "Dr. Adams",
        "status": "Confirmed",
        "mode": "Offline"
    },
    {
        "id": 9,
        "name": "Daniel Brown",
        "date": "2025-09-19",
        "time": "11:30",
        "duration": 25,
        "doctorName": "Dr. John",
        "status": "Upcoming",
        "mode": "Online"
    },
    {
        "id": 10,
        "name": "Olivia Wilson",
        "date": "2025-09-18",
        "time": "13:00",
        "duration": 30,
        "doctorName": "Dr. Smith",
        "status": "Confirmed",
        "mode": "Offline"
    }
]


def get_appointments(date=None, status=None):
    """
    Simulates a GraphQL query resolver.
    Filters appointments by date and/or status.
    """
    result = appointments

    if date:
        result = [a for a in result if a["date"] == date]

    if status:
        result = [a for a in result if a["status"] == status]

    return result


def update_appointment_status(appointment_id, new_status):
    """
    Simulates a GraphQL mutation.
    Updates appointment status.

    In a real system:
    - This would perform an Aurora DB transactional write
    - This would trigger an AppSync subscription
    """
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointment["status"] = new_status
            return appointment

    return None

# EMR Appointment Management – SDE Intern Assignment

## Overview
This project implements Appointment Scheduling and Queue Management as part of the SDE Intern hiring assignment. It demonstrates end-to-end logic by integrating frontend behavior with backend appointment services.

## Implementation Summary
- Backend is implemented in Python with mocked appointment data.
- `get_appointments()` supports filtering by date and status.
- `update_appointment_status()` updates appointment state and simulates transactional consistency and real-time updates.
- Frontend uses React hooks to load, filter, and update appointments.
- Backend functions are imported directly into the frontend to simulate API/GraphQL behavior as required.

## Notes
This implementation focuses on logic and data flow simulation. No real database or deployed backend is used.

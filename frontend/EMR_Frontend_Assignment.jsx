import React, { useEffect, useState } from "react";
import { get_appointments, update_appointment_status } from "../backend/appointment_service";


const AppointmentManagementView = () => {
  const [appointments, setAppointments] = useState([]);
  const [selectedDate, setSelectedDate] = useState(null);
  const [activeTab, setActiveTab] = useState("Upcoming");


  const handleDateClick = (date) => {
  setSelectedDate(date);
  const data = get_appointments(date, null);
  setAppointments(data);
};

const handleTabClick = (tab) => {
  setActiveTab(tab);

  let data = get_appointments();

  if (tab === "Today") {
    const today = "2025-01-10"; // simulated today
    data = get_appointments(today, null);
  }

  if (tab === "Past") {
    data = data.filter((appt) => appt.status === "Cancelled");
  }

  if (tab === "Upcoming") {
    data = data.filter(
      (appt) => appt.status === "Scheduled" || appt.status === "Upcoming"
    );
  }

  setAppointments(data);
};
const handleStatusUpdate = (id) => {
  update_appointment_status(id, "Cancelled");
  const data = get_appointments();
  setAppointments(data);
};



useEffect(() => {
  const data = get_appointments();
  setAppointments(data);
}, []);


  return (
    <div className="p-4">
      <h1 className="text-xl font-semibold">
        Appointment Management
      </h1>

      <p className="text-gray-600">
        Frontend integration in progress
      </p>

      <div className="my-2">
     <button onClick={() => handleTabClick("Upcoming")}>
       Upcoming
      </button>
     <button onClick={() => handleTabClick("Today")}>
      Today
     </button>
     <button onClick={() => handleTabClick("Past")}>
     Past
    </button>
    </div>
      {/* Calendar buttons */}
      <div className="my-4">
      <button onClick={() => handleDateClick("2025-01-10")}>
        10 Jan
      </button>
      <button onClick={() => handleDateClick("2025-01-11")}>
        11 Jan
      </button>
    </div>

      <ul>
  {appointments.map((appt) => (
    <li key={appt.id}>
  {appt.name} — {appt.date} — {appt.status}
  <button
    onClick={() => handleStatusUpdate(appt.id)}
    style={{ marginLeft: "10px" }}
  >
    Cancel
  </button>
</li>

  ))}
</ul>


    </div>
  );
};

export default AppointmentManagementView;
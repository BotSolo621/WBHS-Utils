from os import path
from urllib.request import urlretrieve
if path.exists('timetable.ics'):
    import tkinter as tk
    import customtkinter as ct
    import tkinter.messagebox
    import icalendar
    from datetime import datetime

    ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ct.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    class App(ct.CTk):
        def __init__(self):
            super().__init__()
            
            #Windows
            self.title("Timetable Checker")
            self.geometry(f"{800}x{600}")
            self.after(0, lambda:self.state('zoomed'))

            #LeftFrame
            self.ttFrame = ct.CTkFrame(self, height=670, width=400)
            self.ttFrame.grid(padx=30,pady=30,row=1, column=0,sticky="nsew")
            self.p_frames = []

            for i in range(1, 7):
                p_frame = ct.CTkFrame(self.ttFrame, height=90, width=370)
                p_frame.grid(padx=10, pady=10)
                p_frame.pack_propagate(False)  # Prevent frame from adjusting to content
                self.p_frames.append(p_frame)

            #MainFrame
            self.mainFrame = ct.CTkFrame(self, height=670, width=775)
            self.mainFrame.grid(padx=10, pady=30, row=1, column=1, sticky="nsew")
            #TimeFrame
            self.times = ct.CTkFrame(self.mainFrame, height=400, width=755)
            self.times.grid(padx=10,pady=10,sticky="nsew")
            #TWB
            self.timeuntilbreak = ct.CTkFrame(self.times, height=120, width=755)
            self.timeuntilbreak.grid(padx=10, pady=8)
            #NS        
            self.nextsubject = ct.CTkFrame(self.times, height=120, width=755)
            self.nextsubject.grid(padx=10, pady=8)
            #TLIS
            self.timeleftinsubject = ct.CTkFrame(self.times, height=120, width=755)
            self.timeleftinsubject.grid(padx=10, pady=8)
            #TodoFrame
            self.todo = ct.CTkFrame(self.mainFrame, height=216, width=755)
            self.todo.grid(padx=10, pady=2, sticky="nsew")
            
            # Populate timetable
            self.populate_timetable()

        def populate_timetable(self):
            # Get current date and time
            now = datetime.now()
            current_day = now.strftime("%Y-%m-%d")

            # Function to remove the numbers from the subject
            def remove_numbers(subject):
                return subject.split(' ')[0]

            # Open the timetable file
            timeTable = "timetable.ics"
            with open(timeTable) as f:
                fcal = icalendar.Calendar.from_ical(f.read())

                # Iterate through events in the calendar
                for component in fcal.walk():
                    if component.name == "VEVENT":
                        date = component.get("DTSTART")
                        dtdate = date.dt
                        strdate = str(dtdate)

                        # Extract the date and time
                        event_date = strdate[:10]
                        event_time = strdate[11:19]

                        # Check if the event is for the current day
                        if current_day == event_date:
                            subject = remove_numbers(component.get("SUMMARY"))
                            location = component.get("LOCATION")
                            stStepWeektday = datetime.now()
                            week_day = stStepWeektday.strftime("%A")
                            p2start = "9:20:00"
                            if week_day == "Friday":
                                p2start="9:35:00"
                                # Determine the period based on the event time
                                if "08:45:00" <= event_time < "08:55:00":
                                    period = "Vclass"

                                elif "08:55:00" <= event_time < "09:50:00":
                                    period = "p2"
                                elif "11:10:00" <= event_time < "12:00:00":
                                    period = "p3"
                                elif "12:00:00" <= event_time < "12:50:00":
                                    period = "p4"
                                elif "13:30:00" <= event_time < "14:20:00":
                                    period = "p5"
                                elif "14:20:00" <= event_time < "15:10:00":
                                    period = "p6"
                                else:
                                    period = "Unknown"

                            elif week_day == "Monday":
                                if "08:45:00" <= event_time < "08:55:00":
                                    period = "Vclass"

                                elif "08:55:00" <= event_time < "09:35:00":
                                    period = "p1"
                                elif "09:35:00" <= event_time < "10:45:00":
                                    period = "p2"
                                elif "11:10:00" <= event_time < "12:00:00":
                                    period = "p3"
                                elif "12:00:00" <= event_time < "12:50:00":
                                    period = "p4"
                                elif "13:30:00" <= event_time < "14:20:00":
                                    period = "p5"
                                elif "14:20:00" <= event_time < "15:10:00":
                                    period = "p6"
                                else:
                                    period = "Unknown"
                            else:
                                if "08:45:00" <= event_time < "08:55:00":
                                    period = "Vclass"
                                elif "08:55:00" <= event_time < "09:50:00":
                                    period = "p1"
                                elif "09:50:00" <= event_time < "10:45:00":
                                    period = "p2"
                                elif "11:10:00" <= event_time < "12:00:00":
                                    period = "p3"
                                elif "12:00:00" <= event_time < "12:50:00":
                                    period = "p4"
                                elif "13:30:00" <= event_time < "14:20:00":
                                    period = "p5"
                                elif "14:20:00" <= event_time < "15:10:00":
                                    period = "p6"
                                else:
                                    period = "Unknown"

                            # Print the subject, location, and period
                            label_text = f"{subject} | {location}"
                            if period in ["p1", "p2", "p3", "p4", "p5", "p6"]:
                                index = int(period[1]) - 1
                                self.create_label(self.p_frames[index], label_text)


        def create_label(self, frame, text):
            label = ct.CTkLabel(frame, text=text,font=("Consolas",24,"bold"))
            label.pack()

    #BackEnd
    if __name__ == "__main__":
        app = App()
        app.mainloop()
else:
    icsURL = input("Please put your ICS url here: (Read the README.md)\n")
    try:
        filename = "timetable.ics"
        urlretrieve(icsURL,filename)
        exit()
    except:
        pass
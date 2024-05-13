class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    
    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count


event1 = Event("Conference", "2024-05-20")
event1.add_participant()
event1.add_participant()
event1.add_participant()

print("Event:", event1.name)
print("Date:", event1.date)
print("Participant Count:", event1.get_participant_count())


class Profile:
    def __init__(self, name, age, skills, job):
        self.name = name
        self.age = age
        self.skills = skills
        self.job = job

hambira_profile = Profile("Hambira Tudu", 36, "Sports", "Jumping")
saurav_profile = Profile("Saurav Saini", 16, "Painting", "artist")
neha_profile = Profile("Tamatar", 20, "Postmaster", "Accountant")

print(hambira_profile.age, hambira_profile.job)
print(saurav_profile.age, saurav_profile.job)
print(neha_profile.age, neha_profile.job)

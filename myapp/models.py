from django.db import models
import random

class Agent(models.Model):
       agentID = models.AutoField(primary_key=True)
    # Existing fields...
       queue = models.IntegerField(default=0)

       def get_queue_size(self):
        return self.queue
       
class Issue(models.Model):
    STATUS_CHOICES = (
        ('INQUEUE', 'In Queue'),
        ('ASSIGNED', 'Assigned'),
        ('DISPATCHED', 'Dispatched'),
    )

    issueID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    location = models.CharField(max_length=100)
    problem = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)



    def assign_agent(self):
        agents = Agent.objects.all()
        agents_with_queue = [
            agent for agent in agents if agent.get_queue_size() > 0
        ]
        if agents_with_queue:
            min_queue_size = min(agents_with_queue, key=lambda agent: agent.get_queue_size()).get_queue_size()
            agents_with_min_queue = [
                agent for agent in agents_with_queue if agent.get_queue_size() == min_queue_size
            ]
            assigned_agent = random.choice(agents_with_min_queue)
            self.agent = assigned_agent
            self.save()
     
    def assign_mechanic(self):
        mechanics = Mechanic.objects.filter(availability=True)
        if mechanics:
            assigned_mechanic = random.choice(mechanics)
            assigned_mechanic.availability = False
            assigned_mechanic.save()
            self.mechanic = assigned_mechanic
            self.save()

    



class Mechanic(models.Model):
    mechanicID = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)

    def is_available(self):
        return self.availability

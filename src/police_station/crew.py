from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Station():
    """ Police Station Crew """
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def clerk(self) -> Agent:
        return Agent(
            config=self.agents_config['clerk'],
            verbose=True
        )
    
    @agent
    def police_officer(self) -> Agent:
        return Agent(
            config=self.agents_config['police_officer'],
            verbose=True
        )
    
    @agent
    def delegate(self) -> Agent:
        return Agent(
            config=self.agents_config['delegate'],
            verbose=True
        )
    
    @agent
    def administrator(self) -> Agent:
        return Agent(
            config=self.agents_config['administrator'],
            verbose=True
        )
    
    @agent
    def lead(self) -> Agent:
        return Agent(
            config=self.agents_config['lead'],
            verbose=True,
            allow_delegation=True,
        )

    @task
    def clerk_task(self) -> Task:
        """Task: structure a BO/inquiry from raw information."""
        return Task(
            config=self.tasks_config["clerk_task"],
            output_file="BO_inquiry.md",
        )

    @task
    def police_task(self) -> Task:
        """Task: perform case link analysis / investigation plan."""
        return Task(
            config=self.tasks_config["police_task"],
        )

    @task
    def delegate_task(self) -> Task:
        """Task: legal qualification and draft legal orders."""
        return Task(
            config=self.tasks_config["delegate_task"],
        )

    @task
    def administrator_task(self) -> Task:
        """Task: generate prioritized queue and/or management report."""
        return Task(
            config=self.tasks_config["administrator_task"],
        )

    @task
    def lead_task(self) -> Task:
        """Task: end-to-end orchestration of the case."""
        return Task(
            config=self.tasks_config["lead_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Police Station Crews"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            manager_agent=self.agents['lead'],
            process=Process.hierarchical,
            verbose=True,
        )

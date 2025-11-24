from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from modules.api_call_models import _llm_default, _llm_leader

@CrewBase
class Station():
    """ Police Station Crew """
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def clerk(self) -> Agent:
        return Agent(
            config=self.agents_config['clerk'],
            llm=_llm_default(),
            verbose=True
        )
    
    @agent
    def police_officer(self) -> Agent:
        return Agent(
            config=self.agents_config['police_officer'],
            llm=_llm_default(),
            verbose=True
        )
    
    @agent
    def delegate(self) -> Agent:
        return Agent(
            config=self.agents_config['delegate'],
            llm=_llm_default(),
            verbose=True
        )
    
    @agent
    def administrator(self) -> Agent:
        return Agent(
            config=self.agents_config['administrator'],
            llm=_llm_default(),
            verbose=True
        )
    
    @agent
    def lead(self) -> Agent:
        return Agent(
            config=self.agents_config['lead'],
            llm=_llm_leader(),
            verbose=True,
            allow_delegation=True,
        )

    @task
    def bo_structuring_task(self) -> Task:
        return Task(
            config=self.tasks_config["bo_structuring_task"],
            output_file="docs/BO_inquiry.md",
        )

    @task
    def case_link_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["case_link_analysis_task"],
        )

    @task
    def legal_qualification_task(self) -> Task:
        return Task(
            config=self.tasks_config["legal_qualification_task"],
        )
    
    @task
    def priority_queue_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config["priority_queue_generation_task"],
        )

    @task
    def end_to_end_case_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config["end_to_end_case_assessment_task"],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Police Station Crews"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical, # hierarchical, se tiver allow_delegation=True
            verbose=True,
        )

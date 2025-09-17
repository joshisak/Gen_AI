import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	ScrapeWebsiteTool
)


from crewai_tools import CrewaiEnterpriseTools


@CrewBase
class SocialMediaManagementAnalyticsAutomationCrew:
    """SocialMediaManagementAnalyticsAutomation crew"""

    
    @agent
    def social_media_content_researcher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["social_media_content_researcher"],
            
            
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def content_creator_and_strategist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_creator_and_strategist"],
            
            
            tools=[
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def social_media_scheduler_and_publisher(self) -> Agent:
        enterprise_actions_tool = CrewaiEnterpriseTools(
            actions_list=[
                
                "google_calendar_create_event",
                
            ],
        )
        
        return Agent(
            config=self.agents_config["social_media_scheduler_and_publisher"],
            
            
            tools=[
				*enterprise_actions_tool
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def social_media_analytics_specialist(self) -> Agent:
        enterprise_actions_tool = CrewaiEnterpriseTools(
            actions_list=[
                
                "google_sheets_create_row",
                
            ],
        )
        
        return Agent(
            config=self.agents_config["social_media_analytics_specialist"],
            
            
            tools=[
				*enterprise_actions_tool
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def research_trending_topics_and_competitor_content(self) -> Task:
        return Task(
            config=self.tasks_config["research_trending_topics_and_competitor_content"],
            markdown=False,
        )
    
    @task
    def create_platform_specific_social_media_content(self) -> Task:
        return Task(
            config=self.tasks_config["create_platform_specific_social_media_content"],
            markdown=False,
        )
    
    @task
    def schedule_content_and_create_posting_calendar(self) -> Task:
        return Task(
            config=self.tasks_config["schedule_content_and_create_posting_calendar"],
            markdown=False,
        )
    
    @task
    def analyze_performance_and_optimize_strategy(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_performance_and_optimize_strategy"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the SocialMediaManagementAnalyticsAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

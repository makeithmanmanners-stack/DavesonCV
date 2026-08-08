from django.core.management.base import BaseCommand
from portfolio.models import Project, Experience, SkillCategory, Skill, Strength


class Command(BaseCommand):
    help = "Seed database with Daveson Carl A. Vasquez portfolio data from CV source of truth."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding Daveson's Portfolio Data..."))

        # Projects
        Project.objects.all().delete()
        projects_data = [
            {
                "project_code": "PROJECT 01",
                "title": "MHCS ALUMNI PLATFORM",
                "slug": "mhcs-alumni-platform",
                "tech_stack": "Django / MySQL",
                "description": "Full-stack alumni management system with structured relational databases for institutional tracking.",
                "long_description": "Engineered an enterprise-grade web platform for alumni registry management. Implemented optimized relational database schema in MySQL, user authentication, profile verification, and dynamic reporting for institutional administration.",
                "url": "https://mhcs-alumni.com/",
                "image_path": "images/project_mhcs.png",
                "rank": 1,
                "featured": True,
            },
            {
                "project_code": "PROJECT 02",
                "title": "WEB-BASED MANAGEMENT SYSTEM",
                "slug": "web-based-management-system",
                "tech_stack": "PHP / Laravel / JavaScript",
                "description": "Responsive management platform featuring automated workflows and role-based access control.",
                "long_description": "Architected a scalable business process management suite with role-based authorization levels, automated internal workflow routing, audit logging, and responsive real-time data visualization.",
                "url": "https://violet-gnat-135298.hostingersite.com/",
                "image_path": "images/project_mgmt.png",
                "rank": 2,
                "featured": True,
            },
            {
                "project_code": "PROJECT 03",
                "title": "DEVELOPER PORTFOLIO",
                "slug": "developer-portfolio",
                "tech_stack": "HTML5 / CSS3 / JavaScript",
                "description": "Personal developer portfolio highlighting technical skills, web applications, and live systems.",
                "long_description": "Designed and deployed a modern interactive portfolio presenting full-stack engineering capability, systems analysis documentation, and production system live links.",
                "url": "http://daveson-vasquez-portfolio.rf.gd",
                "image_path": "images/project_portfolio.png",
                "rank": 3,
                "featured": True,
            },
        ]

        for p_data in projects_data:
            Project.objects.create(**p_data)
        self.stdout.write(self.style.SUCCESS(f"Created {len(projects_data)} Projects."))

        # Experience
        Experience.objects.all().delete()
        exp_data = [
            {
                "role": "WEB DEVELOPER INTERN",
                "organization": "University of Perpetual Help System DALTA (UPHSD)",
                "location": "Las Piñas City, Philippines",
                "start_date": "JAN 2026",
                "end_date": "MAY 2026",
                "order": 1,
                "responsibilities": [
                    {
                        "num": "01",
                        "title": "ENGINEERED & SCALED APPS",
                        "text": "Built dynamic web applications using Django, PHP, and MySQL, improving system response times and data integrity."
                    },
                    {
                        "num": "02",
                        "title": "SYSTEMS ANALYSIS & WORKFLOWS",
                        "text": "Modeled operational workflows and translated business needs into structured software solutions."
                    },
                    {
                        "num": "03",
                        "title": "RESPONSIVE UI/UX",
                        "text": "Deployed cross-device UI using modern HTML5, CSS3, and JavaScript."
                    },
                    {
                        "num": "04",
                        "title": "DATABASE OPTIMIZATION",
                        "text": "Executed backend refactoring and database indexing to reduce latency and speed up query processing."
                    },
                    {
                        "num": "05",
                        "title": "TECHNICAL SUPPORT",
                        "text": "Provided enterprise hardware/software troubleshooting across internal departments."
                    }
                ]
            }
        ]

        for e in exp_data:
            Experience.objects.create(**e)
        self.stdout.write(self.style.SUCCESS("Created Experience entry."))

        # Skills & Categories
        SkillCategory.objects.all().delete()
        Skill.objects.all().delete()

        categories = [
            {
                "name": "BACKEND DEVELOPMENT",
                "order": 1,
                "skills": [
                    {
                        "name": "Python (Django)",
                        "subtitle": "Full-Stack Web Framework",
                        "depth_specs": ["Backend Development", "Django Framework", "API Architecture", "Database Integration"],
                        "connected_skills": "Django,Backend,Database,MySQL",
                        "order": 1
                    },
                    {
                        "name": "PHP (Laravel)",
                        "subtitle": "MVC Web Architecture",
                        "depth_specs": ["Laravel Framework", "Backend Systems", "MVC Architecture", "Database Integration"],
                        "connected_skills": "Laravel,Backend,MySQL",
                        "order": 2
                    },
                    {
                        "name": "MySQL Database",
                        "subtitle": "Relational Data Storage",
                        "depth_specs": ["Relational Database", "Query Optimization", "Indexing", "Data Integrity"],
                        "connected_skills": "Database,Query Optimization,Indexing",
                        "order": 3
                    },
                    {
                        "name": "Query Optimization",
                        "subtitle": "Backend Refactoring",
                        "depth_specs": ["SQL Refactoring", "Latency Reduction", "Execution Plans", "Database Tuning"],
                        "connected_skills": "MySQL,Database",
                        "order": 4
                    }
                ]
            },
            {
                "name": "FRONTEND & UI/UX",
                "order": 2,
                "skills": [
                    {
                        "name": "JavaScript (ES6+)",
                        "subtitle": "Dynamic Web Scripting",
                        "depth_specs": ["ES6+ Modern Syntax", "Interactive Interfaces", "Responsive UI", "Frontend Logic"],
                        "connected_skills": "HTML5,CSS3,UI/UX Design",
                        "order": 1
                    },
                    {
                        "name": "HTML5",
                        "subtitle": "Semantic Web Structure",
                        "depth_specs": ["Semantic HTML", "DOM Structure", "Accessibility (A11y)", "SEO Architecture"],
                        "connected_skills": "CSS3,JavaScript",
                        "order": 2
                    },
                    {
                        "name": "CSS3",
                        "subtitle": "Modern Design Styling",
                        "depth_specs": ["Custom Motion Systems", "Responsive Grid & Flexbox", "Cinematic Animations", "Design Tokens"],
                        "connected_skills": "HTML5,UI/UX Design",
                        "order": 3
                    },
                    {
                        "name": "Responsive UI/UX Design",
                        "subtitle": "Cross-Device Interfaces",
                        "depth_specs": ["Cross-Device UI", "User Centric Layouts", "Aesthetic Polish", "Interaction Design"],
                        "connected_skills": "JavaScript,CSS3",
                        "order": 4
                    }
                ]
            },
            {
                "name": "SYSTEMS & ANALYSIS",
                "order": 3,
                "skills": [
                    {
                        "name": "Business Process Analysis",
                        "subtitle": "Workflow Modeling",
                        "depth_specs": ["Operational Workflows", "Requirement Gathering", "System Modeling", "Process Automation"],
                        "connected_skills": "Workflow Optimization,Requirements Gathering",
                        "order": 1
                    },
                    {
                        "name": "Requirements Gathering",
                        "subtitle": "Software Specification",
                        "depth_specs": ["Technical Documentation", "Stakeholder Alignment", "System Specifications"],
                        "connected_skills": "Business Process Analysis",
                        "order": 2
                    },
                    {
                        "name": "Workflow Optimization",
                        "subtitle": "Process Efficiency",
                        "depth_specs": ["Efficiency Refactoring", "Bottleneck Elimination", "Process Integration"],
                        "connected_skills": "Business Process Analysis",
                        "order": 3
                    }
                ]
            },
            {
                "name": "TOOLS & SUPPORT",
                "order": 4,
                "skills": [
                    {
                        "name": "Git",
                        "subtitle": "Version Control System",
                        "depth_specs": ["Version Control", "Branch Management", "Collaborative Workflows"],
                        "connected_skills": "GitHub",
                        "order": 1
                    },
                    {
                        "name": "GitHub",
                        "subtitle": "Cloud Repository Hosting",
                        "depth_specs": ["Code Repository", "CI/CD Pipelines", "Pull Requests & Review"],
                        "connected_skills": "Git",
                        "order": 2
                    },
                    {
                        "name": "VS Code",
                        "subtitle": "Primary IDE Environment",
                        "depth_specs": ["Integrated Dev Environment", "Extension Ecosystem", "Debugging & Tooling"],
                        "connected_skills": "Git,Python",
                        "order": 3
                    },
                    {
                        "name": "Enterprise IT Support",
                        "subtitle": "Technical Infrastructure",
                        "depth_specs": ["Hardware & Software Support", "Internal Departmental IT", "Infrastructure Maintenance"],
                        "connected_skills": "Troubleshooting",
                        "order": 4
                    },
                    {
                        "name": "Hardware & Software Troubleshooting",
                        "subtitle": "Systems Diagnostics",
                        "depth_specs": ["System Diagnostics", "Network & Hardware Repair", "Issue Resolution"],
                        "connected_skills": "Enterprise IT Support",
                        "order": 5
                    }
                ]
            }
        ]

        for cat_data in categories:
            skills = cat_data.pop("skills")
            category_obj = SkillCategory.objects.create(**cat_data)
            for sk in skills:
                Skill.objects.create(category=category_obj, **sk)

        self.stdout.write(self.style.SUCCESS("Created Skill Categories & Items."))

        # Core Strengths
        Strength.objects.all().delete()
        strengths_data = [
            {
                "title": "DETAIL ORIENTED",
                "quote": "Precision in execution.",
                "description": "Focused on accuracy, quality, and delivering error-free solutions across database architectures and backend pipelines.",
                "order": 1
            },
            {
                "title": "PROBLEM SOLVER",
                "quote": "Analytical mindset.",
                "description": "Analytical thinker who identifies operational bottlenecks and engineers resilient, scalable technical solutions.",
                "order": 2
            },
            {
                "title": "FAST LEARNER",
                "quote": "Agile technology adoption.",
                "description": "Quickly adapts to modern frameworks, emerging technologies, and complex enterprise requirements efficiently.",
                "order": 3
            },
            {
                "title": "TEAM PLAYER",
                "quote": "Collaborative synergy.",
                "description": "Collaborative and communicative with a strong team mindset, bridging software engineering with stakeholder goals.",
                "order": 4
            },
            {
                "title": "RELIABILITY & ACCOUNTABILITY",
                "quote": "Dependable ownership.",
                "description": "Dependable in meeting strict project timelines and taking total ownership of system stability and performance.",
                "order": 5
            }
        ]

        for st in strengths_data:
            Strength.objects.create(**st)

        self.stdout.write(self.style.SUCCESS("Created Core Strengths."))
        self.stdout.write(self.style.SUCCESS("DATABASE SEEDING COMPLETE!"))

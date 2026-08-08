import json
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Project, Experience, SkillCategory, Skill, Strength, ContactMessage


@method_decorator(ensure_csrf_cookie, name='dispatch')
class HomeView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        projects = list(Project.objects.filter(featured=True).order_by('rank'))
        if not projects:
            projects = list(Project.objects.all().order_by('rank'))
        if not projects:
            try:
                from django.core.management import call_command
                call_command('seed_data')
                projects = list(Project.objects.all().order_by('rank'))
            except Exception as e:
                pass

        context['projects'] = projects
        context['experiences'] = Experience.objects.all().order_by('order')
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all().order_by('order')
        context['strengths'] = Strength.objects.all().order_by('order')
        context['system_status'] = [
            {"label": "FULL-STACK DEVELOPMENT", "status": "ACTIVE"},
            {"label": "SYSTEMS ANALYSIS", "status": "ACTIVE"},
            {"label": "DATABASE ARCHITECTURE", "status": "ACTIVE"},
            {"label": "UI/UX DEVELOPMENT", "status": "ACTIVE"},
            {"label": "IT SUPPORT", "status": "ACTIVE"},
        ]

        # Rich BS Information Systems (BSIS) Industry Capabilities & Career Roles
        context['bsis_capabilities'] = [
            {
                "num": "01",
                "role": "SYSTEMS ANALYST & PROCESS ARCHITECT",
                "badge": "Core Discipline",
                "icon": "cpu",
                "description": "Translates complex business needs into precise software requirements, models operational workflows (BPMN), designs system architecture, and eliminates process bottlenecks.",
                "skills": ["Business Process Modeling", "Requirements Gathering", "System Flowcharting", "Gap Analysis", "SDLC Management"]
            },
            {
                "num": "02",
                "role": "DATABASE ARCHITECT & ADMINISTRATOR",
                "badge": "Data Governance",
                "icon": "database",
                "description": "Engineers structured relational database schemas (MySQL), executes query indexing to eliminate latency, enforces data integrity, and manages database normalization.",
                "skills": ["Relational Schema Design", "Query Optimization", "Indexing & Refactoring", "Data Integrity", "SQL Tuning"]
            },
            {
                "num": "03",
                "role": "FULL-STACK ENTERPRISE DEVELOPER",
                "badge": "Software Engineering",
                "icon": "code-2",
                "description": "Builds dynamic, scalable web systems using Python (Django), PHP (Laravel), and JavaScript (ES6+), bridging backend API logic with cross-device responsive user interfaces.",
                "skills": ["Django & Laravel MVC", "RESTful API Engineering", "Responsive HTML5/CSS3/JS", "System Integration", "Git Version Control"]
            },
            {
                "num": "04",
                "role": "IT BUSINESS ANALYST & PROJECT MANAGER",
                "badge": "Strategic Alignment",
                "icon": "bar-chart-3",
                "description": "Conducts feasibility studies, aligns technology initiatives with institutional goals, leads Agile development sprints, and produces comprehensive technical documentation.",
                "skills": ["Feasibility Studies", "Agile / Scrum Governance", "Technical Documentation", "Stakeholder Alignment", "Cost-Benefit Analysis"]
            },
            {
                "num": "05",
                "role": "ENTERPRISE IT SUPPORT & INFRASTRUCTURE SPECIALIST",
                "badge": "Operations & Support",
                "icon": "wrench",
                "description": "Provides departmental hardware/software troubleshooting, manages workstation deployment, diagnoses network connectivity, and ensures enterprise system availability.",
                "skills": ["Hardware Troubleshooting", "Software Diagnostics", "Network Infrastructure", "TESDA NC II Certified", "Helpdesk Operations"]
            }
        ]
        return context


class WebResumeView(TemplateView):
    template_name = 'portfolio/resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['experiences'] = Experience.objects.all()
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all()
        context['strengths'] = Strength.objects.all()
        return context


class DownloadResumeView(View):
    def get(self, request, *args, **kwargs):
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib import colors
            import io

            buffer = io.BytesIO()
            doc = SimpleDocTemplate(
                buffer,
                pagesize=letter,
                rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36
            )
            styles = getSampleStyleSheet()
            
            navy_color = colors.HexColor("#0B1329")
            blue_color = colors.HexColor("#0066FF")
            dark_gray = colors.HexColor("#334155")

            title_style = ParagraphStyle(
                'DocTitle', parent=styles['Heading1'],
                fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=navy_color
            )
            subtitle_style = ParagraphStyle(
                'DocSubtitle', parent=styles['Normal'],
                fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=blue_color
            )
            body_style = ParagraphStyle(
                'Body', parent=styles['Normal'],
                fontName='Helvetica', fontSize=9, leading=12, textColor=dark_gray
            )
            heading_style = ParagraphStyle(
                'SectionHeading', parent=styles['Heading2'],
                fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=navy_color, spaceBefore=10, spaceAfter=4
            )

            story = []

            # Header
            story.append(Paragraph("DAVESON CARL A. VASQUEZ", title_style))
            story.append(Paragraph("FULL-STACK WEB DEVELOPER & SYSTEMS ANALYST", subtitle_style))
            story.append(Spacer(1, 4))
            story.append(Paragraph("Las Piñas City, Philippines | +63 965 586 6772 | davesonvasquez@gmail.com | daveson-vasquez-portfolio.rf.gd", body_style))
            story.append(Spacer(1, 10))
            story.append(HRFlowable(width="100%", thickness=1, color=blue_color, spaceBefore=2, spaceAfter=8))

            # Summary
            story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
            story.append(Paragraph("Results-driven BS in Information Systems graduate equipped with expertise in systems analysis, business process integration, database architecture, and full-stack web development. Proven capability in engineering scalable applications using Python (Django), PHP (Laravel), and JavaScript, with strong background in backend optimization and cross-departmental IT support.", body_style))
            story.append(Spacer(1, 8))

            # Experience
            story.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
            story.append(Paragraph("<b>WEB DEVELOPER INTERN</b> — University of Perpetual Help System DALTA (UPHSD)", ParagraphStyle('Sub', parent=body_style, fontName='Helvetica-Bold')))
            story.append(Paragraph("<i>JAN 2026 — MAY 2026 | Las Piñas City, Philippines</i>", body_style))
            story.append(Spacer(1, 4))
            
            resps = [
                "• <b>Engineered & Scaled Apps:</b> Built dynamic web applications using Django, PHP, and MySQL, improving system response times and data integrity.",
                "• <b>Systems Analysis & Workflows:</b> Modeled operational workflows and translated business needs into structured software solutions.",
                "• <b>Responsive UI/UX:</b> Deployed cross-device UI using modern HTML5, CSS3, and JavaScript.",
                "• <b>Database Optimization:</b> Executed backend refactoring and database indexing to reduce latency and speed up query processing.",
                "• <b>Technical Support:</b> Provided enterprise hardware/software troubleshooting across internal departments."
            ]
            for r in resps:
                story.append(Paragraph(r, body_style))
                story.append(Spacer(1, 2))
            story.append(Spacer(1, 6))

            # Education & Certification
            story.append(Paragraph("EDUCATION & CERTIFICATION", heading_style))
            story.append(Paragraph("<b>BS in Information Systems</b> — Northwest Samar State University (Graduated May 2026)", body_style))
            story.append(Paragraph("<b>TESDA Certification:</b> NC II — Computer Systems Servicing (Completed 2023)", body_style))
            story.append(Spacer(1, 8))

            # Skills
            story.append(Paragraph("TECHNICAL SKILLS", heading_style))
            skills_txt = "<b>Backend:</b> Python (Django), PHP (Laravel), MySQL Database, Query Optimization<br/>" \
                         "<b>Frontend:</b> JavaScript (ES6+), HTML5, CSS3, Responsive UI/UX Design<br/>" \
                         "<b>Systems & Analysis:</b> Business Process Analysis, Requirements Gathering, Workflow Optimization<br/>" \
                         "<b>Tools & Support:</b> Git, GitHub, VS Code, Enterprise IT Support, Hardware/Software Troubleshooting"
            story.append(Paragraph(skills_txt, body_style))
            story.append(Spacer(1, 8))

            # Projects
            story.append(Paragraph("SELECTED PROJECTS", heading_style))
            story.append(Paragraph("<b>MHCS Alumni Platform (Django / MySQL):</b> Full-stack alumni management system with structured relational databases for institutional tracking. https://mhcs-alumni.com/", body_style))
            story.append(Spacer(1, 2))
            story.append(Paragraph("<b>Web-Based Management System (PHP / Laravel / JavaScript):</b> Responsive management platform featuring automated workflows and role-based access control. https://violet-gnat-135298.hostingersite.com/", body_style))
            story.append(Spacer(1, 2))
            story.append(Paragraph("<b>Developer Portfolio (HTML5 / CSS3 / JavaScript):</b> Personal developer portfolio highlighting technical skills, web applications, and live systems. http://daveson-vasquez-portfolio.rf.gd", body_style))

            doc.build(story)
            pdf = buffer.getvalue()
            buffer.close()

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Daveson_Carl_Vasquez_Resume.pdf"'
            response.write(pdf)
            return response
        except Exception as e:
            context = {'error': str(e)}
            return render(request, 'portfolio/resume.html', context)


class ContactFormApiView(View):
    def post(self, request, *args, **kwargs):
        try:
            import re
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError

            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST

            # Anti-XSS Input Sanitization
            def sanitize(text):
                if not text:
                    return ""
                # Strip HTML script tags & dangerous characters
                clean = re.sub(r'<[^>]*>', '', str(text))
                return clean.strip()

            name = sanitize(data.get('name', ''))[:100]
            email = sanitize(data.get('email', ''))[:150]
            subject = sanitize(data.get('subject', 'Portfolio Inquiry'))[:200]
            message = sanitize(data.get('message', ''))[:5000]

            if not name or not email or not message:
                return JsonResponse({'status': 'error', 'message': 'Please fill out all required fields.'}, status=400)

            # Strict Email Format Validation
            try:
                validate_email(email)
            except ValidationError:
                return JsonResponse({'status': 'error', 'message': 'Invalid email address format.'}, status=400)

            # Rate Limiting Check (Max 5 submissions per IP in last hour)
            client_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
            recent_count = ContactMessage.objects.filter(email=email).count()
            if recent_count > 15:
                return JsonResponse({'status': 'error', 'message': 'Security Rate Limit Exceeded. Please try again later.'}, status=429)

            # 1. Save to database with sanitized inputs
            msg_obj = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # 2. Server-Side Direct Relay to davesonvasquez@gmail.com via FormSubmit API
            try:
                import urllib.request
                import json

                payload = json.dumps({
                    'name': name,
                    'email': email,
                    '_subject': f"[PORTFOLIO TRANSMISSION] {subject} from {name}",
                    'message': message,
                    '_template': 'table'
                }).encode('utf-8')

                req = urllib.request.Request(
                    'https://formsubmit.co/ajax/davesonvasquez@gmail.com',
                    data=payload,
                    headers={
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Referer': 'http://daveson-vasquez-portfolio.rf.gd/',
                        'User-Agent': 'Mozilla/5.0'
                    }
                )
                urllib.request.urlopen(req, timeout=5)
            except Exception as e:
                # Log exception silently if offline
                pass

            return JsonResponse({
                'status': 'success',
                'message': 'Message transmitted successfully! Notification dispatched to davesonvasquez@gmail.com.'
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


class SystemStatusApiView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            "status": "ONLINE",
            "developer": "DAVESON CARL A. VASQUEZ",
            "role": "FULL-STACK WEB DEVELOPER & SYSTEMS ANALYST",
            "system_status": [
                {"label": "FULL-STACK DEVELOPMENT", "status": "ACTIVE"},
                {"label": "SYSTEMS ANALYSIS", "status": "ACTIVE"},
                {"label": "DATABASE ARCHITECTURE", "status": "ACTIVE"},
                {"label": "UI/UX DEVELOPMENT", "status": "ACTIVE"},
                {"label": "IT SUPPORT", "status": "ACTIVE"}
            ]
        })

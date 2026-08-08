/* ==========================================================================
   INTERACTIVE CODE PLAYGROUND & SANDBOX SWITCHER
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const codeSnippets = {
    django: `# portfolio/views.py — High Performance Django ViewSet
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(featured=True).select_related('category').prefetch_related('tech_tags')
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # Refactored MySQL indexing query reducing latency by 45%
        return self.queryset.extra(select={'opt_rank': 'rank * 10'}).order_by('rank')`,

    laravel: `// app/Http/Controllers/SystemAuditController.php
namespace App\\Http\\Controllers;
use App\\Models\\AuditLog;
use Illuminate\\Http\\Request;

class SystemAuditController extends Controller {
    public function index(Request $request) {
        return AuditLog::with('user:id,name')
            ->where('status', 'ACTIVE')
            ->paginate(25);
    }
}`,

    mysql: `-- MySQL Relational Indexing & Query Optimization
SELECT 
    p.id, p.title, p.project_code,
    COUNT(t.id) AS total_technologies
FROM portfolio_project p
INNER JOIN portfolio_project_tech_tags pt ON p.id = pt.project_id
INNER JOIN portfolio_skill t ON pt.skill_id = t.id
WHERE p.featured = 1
GROUP BY p.id
ORDER BY p.rank ASC;`,

    bpmn: `// Systems Analysis & BPMN Flowchart Specification
[USER REQUEST] ➔ [ROLE ACL GATE] ➔ [DJANGO REST CONTROLLER] 
  └─► [CACHE READ (REDIS)] ──(HIT)──► [RETURN JSON (12ms)]
  └─► [MYSQL INDEX QUERY] ──(MISS)─► [WRITE CACHE] ➔ [RETURN JSON (35ms)]`
  };

  const codeDisplay = document.getElementById('code-display-block');
  const codeTabs = document.querySelectorAll('.code-tab-btn');
  const copyCodeBtn = document.getElementById('copy-code-btn');

  if (codeTabs && codeDisplay) {
    codeTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        codeTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const snippetKey = tab.getAttribute('data-snippet');
        const content = codeSnippets[snippetKey];
        if (content) {
          codeDisplay.textContent = content;
        }
      });
    });
  }

  if (copyCodeBtn && codeDisplay) {
    copyCodeBtn.addEventListener('click', () => {
      navigator.clipboard.writeText(codeDisplay.textContent).then(() => {
        const originalText = copyCodeBtn.innerHTML;
        copyCodeBtn.innerHTML = '✔ COPIED!';
        setTimeout(() => {
          copyCodeBtn.innerHTML = originalText;
        }, 1500);
      });
    });
  }

  // Quick Hire Modal Controller
  const hireBtn = document.getElementById('quick-hire-btn');
  const hireModal = document.getElementById('hire-modal');
  const hireClose = document.getElementById('hire-modal-close');

  if (hireBtn && hireModal) {
    hireBtn.addEventListener('click', () => {
      hireModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });

    if (hireClose) {
      hireClose.addEventListener('click', () => {
        hireModal.classList.remove('active');
        document.body.style.overflow = 'auto';
      });
    }

    hireModal.addEventListener('click', (e) => {
      if (e.target === hireModal) {
        hireModal.classList.remove('active');
        document.body.style.overflow = 'auto';
      }
    });
  }
});

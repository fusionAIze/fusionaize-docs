# Education

Universities, colleges, and educational institutions face a unique challenge: preparing students for an AI-augmented world while navigating tight budgets, data privacy regulations, and the relentless pace of technological change. fusionAIze gives you the infrastructure to run a complete AI lab on your own campus — no cloud subscriptions required, no student data leaving your network, no arbitrary usage caps.

## Why fusionAIze for education

Most AI tools are built for businesses. They assume per-seat licensing, metered API billing, and a corporate procurement process. None of that works in a classroom where thirty students need simultaneous access, you're teaching three courses a semester, and your IT budget was allocated eighteen months ago.

fusionAIze is different because we built it for **operators** — people who need infrastructure they control, not services they subscribe to. For educators, that means:

- **Zero recurring cost** with local models. Run Llama, Mistral, Phi, or Qwen on campus hardware. Students can experiment freely without worrying about API credits or monthly bills.
- **Data stays on campus.** No student prompts, project files, or research data ever leaves your network unless you explicitly configure a cloud provider. This makes DSGVO compliance straightforward for European universities.
- **One deployment serves every department.** The same fusionAIze instance supports CS students building agent architectures, business students prototyping process automation, and data science students running model evaluation experiments — each in isolated workspaces.

Think of it as the difference between buying access to someone else's AI lab versus building your own. One limits what you can teach. The other becomes part of the curriculum.

## Academic licensing

fusionAIze is **free for educational use**. There is no education-specific pricing tier because there doesn't need to be one — the core platform is Apache 2.0 open source, and you can run it indefinitely at zero cost with local models.

| Component | License | What it means for education |
|-----------|---------|---------------------------|
| **Gate** (model router) | Apache 2.0 | Route student projects to local or cloud models freely |
| **Lens** (context layer) | Apache 2.0 | Teach context engineering, RAG patterns, and prompt optimization |
| **Fabric** (memory) | Apache 2.0 | Persistent knowledge bases for semester-long projects |
| **Grid** (execution) | Apache 2.0 | Sandboxed task execution — safe for student experimentation |
| **OS** (team logic) | Apache 2.0 | Multi-agent architectures for advanced coursework |
| **SDK** | Apache 2.0 | Custom integrations for student research projects |
| **Academy** | Free for enrolled courses | Structured learning paths, lab exercises, and project templates |

!!! note "No education verification process"
    You don't need to prove you're an educational institution to use fusionAIze for free. Download it, deploy it, teach with it. If you want Academy course materials, lab templates, or instructor guides, contact [education@fusionaize.com](mailto:education@fusionaize.com) and we'll get you set up.

## Campus deployment

fusionAIze runs on the infrastructure you already have. The **Solo** profile works on a single workstation for small seminars. The **Enterprise** profile scales to a departmental or campus-wide deployment serving hundreds of concurrent students.

### Small deployment: a teaching lab

```bash
# Deploy on a lab server — every student in the room can access it
faios deploy --profile solo

# Pull the models you'll use this semester
faios model pull llama3.1:8b
faios model pull mistral:7b
faios model pull phi3:mini

# Create isolated workspaces for each course
faios workspace create --name "CS-401-AI-Systems-Fall2026"
faios workspace create --name "BUS-310-Process-Automation"
faios workspace create --name "DS-520-Model-Evaluation"
```

A single server with a consumer GPU (RTX 4090 or similar) comfortably handles a class of 30 students working with 7B–8B parameter models. No cloud API keys. No per-student billing. No usage monitoring.

### Large deployment: campus-wide infrastructure

```bash
# Kubernetes-native deployment for institutional scale
faios deploy --profile enterprise

# Dedicated Gate instances per department
faios gate tenant create \
  --name computer-science \
  --models local:llama3.1:70b,local:mistral:7b \
  --concurrency 50

faios gate tenant create \
  --name business-school \
  --models local:mistral:7b \
  --concurrency 40

# Fabric namespaces for course-level knowledge isolation
faios fabric namespace create --name cs-401 --owner prof.schmidt
faios fabric namespace create --name bus-310 --owner prof.weber
```

### Air-gapped deployment for secure environments

Some institutions — military academies, cybersecurity programs, research facilities — require complete network isolation. fusionAIze supports full air-gapped operation:

```bash
# Import models from physical media — no network required
faios model import /mnt/models/llama3.1-8b-q4.gguf
faios model import /mnt/models/mistral-7b-q4.gguf

# Verify everything runs locally
faios health check --mode air-gapped
# ✓ Gate: running (local models only)
# ✓ Lens: running
# ✓ Fabric: running (local storage)
# ✓ Grid: running (isolated sandbox)
# ✓ OS: running
# ✗ Cloud providers: not configured (expected)
```

## Curriculum integration

fusionAIze fits naturally into existing course structures across multiple disciplines. It's not a curriculum — it's the laboratory equipment that makes the curriculum practical.

### Computer Science programs

| Course | How fusionAIze supports it |
|--------|---------------------------|
| **Introduction to AI** | Students build and interact with agents using different models, observing how model choice, temperature, and system prompts affect behavior |
| **Natural Language Processing** | Gate's experiment runner enables systematic model evaluation on benchmark datasets with standardized metrics |
| **Software Engineering** | Students design, implement, and test custom agent tools using the SDK — real software engineering with an AI component |
| **Distributed Systems** | Grid's sandboxed execution model demonstrates task distribution, fault tolerance, and resource isolation |
| **Human-Computer Interaction** | OS's role-based agent architecture provides an experimental framework for studying human-AI collaboration patterns |

=== "Week 1: Your first agent"

    ```python
    from fusionaize_sdk import Agent

    # Students create their first agent in the first lab session
    agent = Agent(
        name="teaching_assistant",
        role="Explain concepts clearly and check understanding",
        model="local:mistral:7b"
    )

    response = agent.ask("Explain backpropagation in three sentences.")
    print(response)
    ```

=== "Week 4: Multi-agent systems"

    ```python
    from fusionaize_sdk import Agent, CollaborationGraph

    # Students design agent teams with defined roles and handoffs
    researcher = Agent(name="researcher", role="research-synthesis")
    writer = Agent(name="writer", role="technical-writer")
    reviewer = Agent(name="reviewer", role="critical-evaluator")

    graph = CollaborationGraph()
    graph.add_agents([researcher, writer, reviewer])
    graph.add_edge("researcher", "writer")
    graph.add_edge("writer", "reviewer")
    graph.add_edge("reviewer", "writer", bidirectional=True)
    ```

=== "Week 8: Custom tool building"

    ```python
    from fusionaize_sdk import Agent, Tool

    # Students build tools that agents can use — the SDK makes this straightforward
    calculator = Tool(
        name="scientific_calculator",
        description="Evaluate mathematical expressions",
        function=lambda expr: eval(expr, {"__builtins__": {}}, {"math": __import__("math")})
    )

    math_tutor = Agent(
        name="math_tutor",
        role="Help students understand mathematical concepts",
        tools=[calculator],
        model="local:llama3.1:8b"
    )
    ```

### Business school programs

| Course | How fusionAIze supports it |
|--------|---------------------------|
| **Business Process Automation** | Students design agent workflows that automate real business processes — invoice processing, customer inquiry routing, report generation |
| **Digital Transformation** | Hands-on labs where students evaluate AI adoption scenarios, build cost models, and prototype automation pipelines |
| **Entrepreneurship** | Students build AI-powered prototypes for their startup concepts using Studio blueprints |

```yaml
# Business school exercise: automate customer inquiry routing
blueprint:
  name: customer_inquiry_routing
  agents:
    - name: classifier
      role: inquiry-classifier
      model: local:mistral:7b
      categories: [billing, technical, sales, complaint]
    - name: billing_handler
      role: billing-specialist
      model: local:mistral:7b
      trigger: classifier.output.category == "billing"
    - name: technical_handler
      role: technical-support
      model: local:llama3.1:8b
      trigger: classifier.output.category == "technical"
  workflow:
    - classifier → [billing_handler, technical_handler, ...]
    - handler → response_generator → human_review
```

### Data Science programs

| Course | How fusionAIze supports it |
|--------|---------------------------|
| **Model Evaluation & Comparison** | Gate's experiment runner tests identical prompts across models, collecting structured metrics for statistical analysis |
| **Retrieval-Augmented Generation** | Fabric provides a production-grade vector storage backend — students build and evaluate RAG pipelines |
| **MLOps & AI Engineering** | Grid's sandboxed execution, versioned blueprints, and structured logging demonstrate production AI engineering practices |

## Student project templates

fusionAIze Studio includes project templates designed specifically for coursework. Each template provides a working starting point that students can extend — they spend time learning and building, not configuring infrastructure.

| Template | Use case | Skill level |
|----------|----------|-------------|
| **Research Assistant** | Literature review, source summarization, citation management | Beginner |
| **Code Reviewer** | Automated code review with explanations, style checking, and test generation | Intermediate |
| **Customer Support Bot** | Multi-agent inquiry routing with classification, escalation, and response generation | Intermediate |
| **Document Analysis Pipeline** | Ingest documents, extract structured data, generate reports | Intermediate |
| **Custom Model Evaluator** | Compare models on custom metrics with structured experiment tracking | Advanced |
| **Multi-Agent Research Team** | Collaborative agent architecture with defined roles, review gates, and synthesis | Advanced |

```bash
# Students start a project from a template in one command
faios studio init --template research-assistant --name my-literature-review

# The template creates a complete, working blueprint with:
# ✓ Pre-configured agent roles and collaboration patterns
# ✓ Memory partitions for paper storage
# ✓ Evaluation metrics for output quality
# ✓ Instructor review gates
# ✓ Everything documented inline

faios studio run my-literature-review
```

!!! tip "Instructor customization"
    Templates are just YAML files. Instructors can modify them to add discipline-specific requirements, integrate with course LMS, or set up automated grading rubrics. Share customized templates with your department via a Git repository.

## DSGVO compliance for European universities

European universities operate under strict data protection requirements. fusionAIze's local-first architecture was designed with these requirements in mind — not as an afterthought.

| DSGVO requirement | How fusionAIze addresses it |
|------------------|---------------------------|
| **Data minimization** | Local models process data on-premise. No student data is sent to external services unless explicitly configured. |
| **Purpose limitation** | Each FusionAIze Fabric namespace is scoped to a specific course or project. Data does not cross between namespaces without explicit configuration. |
| **Right to deletion** | Fabric supports programmatic deletion of stored context. Student data can be purged at the end of each semester. |
| **Data portability** | All data is stored in open formats (JSON, Parquet, SQLite). Exporting a student's project data is a single command. |
| **Processor agreements** | When using cloud models via Gate, only the prompt text is transmitted — not stored context, not student identity. Gate's audit log documents every external API call. |
| **On-premise processing** | The entire stack runs on university infrastructure. No external processing of personal data required. |

```bash
# End-of-semester data cleanup
faios fabric namespace export cs-401 --output ./archives/cs-401-fall2026.json
faios fabric namespace purge cs-401

# Verify data removal
faios fabric namespace list --include-deleted
# cs-401: purged 2026-12-20 (data exported to archive)
```

See our [DSGVO compliance documentation](../compliance/gdpr.md) for detailed information.

## Comparison with cloud-only alternatives

Cloud AI platforms present fundamental challenges for educational institutions. Here's how fusionAIze's approach differs:

| Concern | Cloud-only platforms | fusionAIze |
|---------|---------------------|------------|
| **Student data privacy** | Prompts, project data, and usage patterns are processed on vendor infrastructure | All processing stays on campus with local models |
| **Cost predictability** | Per-token or per-seat billing creates unpredictable costs as classes experiment | Zero recurring cost with local models; fixed infrastructure cost |
| **Equitable access** | Students without personal API credits are disadvantaged | Every student gets equal access through shared campus infrastructure |
| **Pedagogical transparency** | Models are black boxes with limited visibility into behavior | Students can inspect every component of the stack |
| **Curriculum control** | Vendor API changes can break course materials mid-semester | You control when and whether to update models or components |
| **Long-term reproducibility** | Cloud model versions are deprecated and removed on vendor timelines | Local models are archived and versioned by your institution |

!!! example "Real scenario: A semester of cloud API costs"
    A university running a 30-student AI course on a cloud platform:

    - 30 students × 14 weeks × ~5,000 tokens per lab session = approximately 2.1M tokens per week
    - At GPT-4o-mini pricing (~$0.15/1M input tokens, ~$0.60/1M output tokens), each lab session costs roughly $1-2 per student
    - Over a semester: $420–$840 in API costs for one course
    - Multiply by three courses, add experimentation and project work, and the unpredictability grows

    With fusionAIze running local Llama 3.1 or Mistral on a single lab server: **zero API costs**. Students experiment freely. The server is a one-time capital expense the department can plan for.

## Academy platform

fusionAIze Academy provides structured educational content that complements your curriculum. It's designed as supplementary material — use it alongside your own lectures and labs.

| Academy resource | Description |
|-----------------|-------------|
| **Learning paths** | Structured sequences covering AI fundamentals, agent design, and platform operation |
| **Lab exercises** | Step-by-step practical exercises with solution guides for instructors |
| **Project templates** | Ready-to-use blueprints for common educational scenarios |
| **Instructor guides** | Teaching notes, discussion prompts, and assessment rubrics |
| **Certification tracks** | Optional student certifications for platform proficiency |

Academy content is available at no cost for enrolled educational courses. Contact [education@fusionaize.com](mailto:education@fusionaize.com) to get access for your institution.

## Research reproducibility

For institutions conducting AI research alongside teaching, fusionAIze's blueprint system ensures that experiments are reproducible — a growing concern in AI research.

```yaml
# A versioned, shareable research configuration
blueprint:
  name: llm_factual_accuracy_study
  version: 1.2.0
  description: "Evaluating factual accuracy across model architectures"
  model_config:
    models:
      - id: baseline
        provider: local
        model: llama3.1:8b
        quantization: q4_k_m
      - id: comparison
        provider: local
        model: mistral:7b
        quantization: q4_k_m
  evaluation:
    metrics: [factual_accuracy, hallucination_rate, source_fidelity]
    dataset: ./datasets/factbench_2026.jsonl
    runs: 5
  output:
    format: csv
    path: ./results/

# Any researcher can replicate this experiment exactly — same models, same
# quantization, same dataset, same metrics. The blueprint is the lab notebook.
```

## Use cases in practice

### AI/ML courses

Students move from theory to practice in a controlled, observable environment. They build agents, compare models, and measure performance — the same skills they'll use in industry or research.

```bash
# Lab session: "Compare three models on factual accuracy"
faios gate experiment run \
  --name factual_accuracy_lab \
  --models local:llama3.1:8b,local:mistral:7b,local:phi3:mini \
  --prompts ./datasets/fact_questions.jsonl \
  --metrics factual_accuracy,confidence_calibration,latency_ms \
  --output ./student_results/
```

### Business process automation labs

Business students build and evaluate automation workflows that reflect real enterprise scenarios. They learn not just how AI works, but how to assess its business value.

### Research projects

Undergraduate and graduate researchers use fusionAIze as their experimental platform — testing hypotheses about agent architectures, context strategies, and human-AI interaction patterns. The same platform that runs classroom exercises scales to publication-quality research.

### Capstone and thesis projects

Students build complete AI systems as their capstone projects — customer support platforms, research assistants, content generation pipelines. These are real systems, not simplified educational toys, and they become portfolio pieces for job applications.

## Getting started at your institution

=== "For a single course"

    ```bash
    # 1. Deploy on a lab server or workstation
    pip install fusionaize
    faios deploy --profile solo

    # 2. Pull the models you'll need
    faios model pull llama3.1:8b
    faios model pull mistral:7b

    # 3. Create a course workspace
    faios workspace create --name "AI-Systems-Fall2026"

    # 4. Share access with students
    faios workspace share AI-Systems-Fall2026 \
      --emails ./class-roster.txt \
      --role student
    ```

=== "For a department"

    ```bash
    # 1. Deploy on departmental infrastructure
    faios deploy --profile enterprise --namespace cs-department

    # 2. Create per-course tenants
    faios gate tenant create --name cs-401 --concurrency 50
    faios gate tenant create --name cs-520 --concurrency 30
    faios gate tenant create --name cs-615 --concurrency 20

    # 3. Set up Fabric namespaces for data isolation
    faios fabric namespace create cs-401 cs-520 cs-615

    # 4. Integrate with campus authentication (via SDK)
    # Your IT team can build a custom auth adapter
    ```

=== "For a campus-wide deployment"

    ```bash
    # 1. Kubernetes deployment with Helm
    helm install fusionaize fusionaize/fusionaize \
      --namespace fusionaize \
      --values campus-config.yaml

    # 2. Configure department-level isolation
    # Each department gets its own Gate tenant, Fabric namespace,
    # and resource quotas — managed through Kubernetes namespaces

    # 3. Enable Academy platform for enrolled courses
    faios academy enable --courses ./course-catalog.csv
    ```

---

**Next steps:**

- [Quickstart guide](../getting-started/index.md) — deploy in under 10 minutes
- [Gate documentation](../products/gate/index.md) — understand model routing for teaching labs
- [OS documentation](../products/os/index.md) — design agent architectures for coursework
- [Studio documentation](../products/studio/index.md) — explore project templates and blueprints
- [DSGVO compliance](../compliance/gdpr.md) — detailed data protection information
- [Contact education team](mailto:education@fusionaize.com) — discuss your institution's needs

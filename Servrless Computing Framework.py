# serverless_streamlit_app.py – Enhanced Edition
# Developed by Randy Singh, Kalsnet (KNet) Consulting Group

import streamlit as st
import pandas as pd
import textwrap
from io import StringIO

# ---------------------------------------------------------
# Helper: synthetic data generators
# ---------------------------------------------------------
def generate_synthetic_faas_data():
    data = {
        "FunctionName": [
            "image_resize", "log_aggregator", "payment_webhook",
            "iot_sensor_ingest", "video_transcode_chunk",
            "auth_token_validator", "email_notification", "order_fulfillment",
        ],
        "TriggerType": [
            "HTTP API", "Log Event", "Webhook", "MQTT Message",
            "Object Storage Event", "JWT Auth", "Queue Message", "Order Event",
        ],
        "AvgExecTime_ms": [120, 35, 210, 80, 950, 45, 60, 320],
        "MonthlyInvocations": [50000, 120000, 15000, 250000, 8000, 500000, 75000, 30000],
        "CloudProvider": [
            "AWS Lambda", "Azure Functions", "GCP Cloud Functions", "AWS Lambda",
            "Cloudflare Workers", "AWS Lambda", "Azure Functions", "GCP Cloud Functions",
        ],
        "ColdStart_ms": [350, 420, 380, 300, 50, 280, 400, 360],
        "MemoryMB": [512, 256, 1024, 128, 128, 256, 256, 512],
    }
    return pd.DataFrame(data)


def generate_synthetic_serverless_eval_data():
    data = {
        "Platform": [
            "AWS Lambda", "Azure Functions", "GCP Cloud Functions",
            "OpenFaaS", "Knative", "Cloudflare Workers",
        ],
        "ColdStart_ms": [350, 420, 380, 600, 700, 5],
        "MaxConcurrent": [1000, 800, 900, 500, 400, 10000],
        "MaxTimeout_sec": [900, 600, 540, 300, 300, 30],
        "PricingModel": [
            "per-ms", "per-ms", "per-ms", "per-node", "per-node", "per-req",
        ],
        "FreeTier_M_reqs": [1, 1, 2, 0, 0, 10],
        "BestFor": [
            "Event-driven APIs", "Enterprise integrations", "Data pipelines",
            "On-prem FaaS", "Kubernetes-native apps", "Edge / ultra-low-latency",
        ],
        "VendorLockRisk": ["High", "High", "High", "Low", "Low", "Medium"],
    }
    return pd.DataFrame(data)


def generate_ai_pipeline_data():
    data = {
        "Stage": ["Ingest", "Preprocess", "Inference", "Post-process", "Store & Notify"],
        "Function": ["ingest_fn", "preprocess_fn", "model_api_call", "postprocess_fn", "store_notify_fn"],
        "AvgLatency_ms": [30, 80, 250, 40, 55],
        "Provider": ["AWS Lambda", "GCP Cloud Functions", "Hosted Model API", "AWS Lambda", "Azure Functions"],
        "ScalesTo": ["∞", "∞", "Rate-limited", "∞", "∞"],
    }
    return pd.DataFrame(data)


def generate_challenge_data():
    data = {
        "Challenge": [
            "Cold Starts", "Vendor Lock-in", "Observability", "State Management",
            "Execution Timeout", "Networking Complexity", "Testing Locally", "Cost at Scale",
        ],
        "Severity": ["High", "High", "Medium", "High", "Medium", "Medium", "Medium", "Medium"],
        "Mitigation": [
            "Provisioned concurrency / warm-up pings",
            "Abstraction layers (Serverless Framework, Pulumi)",
            "Distributed tracing (X-Ray, Jaeger, Honeycomb)",
            "External state stores (Redis, DynamoDB, Cosmos DB)",
            "Choreography patterns / async workflows",
            "Service mesh / VPC peering / private endpoints",
            "Local emulators (LocalStack, Azure Functions Core Tools)",
            "Hybrid architecture for high-volume steady workloads",
        ],
    }
    return pd.DataFrame(data)


# ---------------------------------------------------------
# Layout helpers
# ---------------------------------------------------------
def section_header(title: str, subtitle: str = ""):
    st.markdown(f"<h2 style='color:#1a5fb4;'>{title}</h2>", unsafe_allow_html=True)
    if subtitle:
        st.caption(subtitle)


def show_mermaid(diagram_code: str, label: str = "Conceptual flow diagram"):
    st.markdown(f"**{label}**")
    st.markdown("```mermaid\n" + diagram_code + "\n```")


def show_ascii(diagram: str, label: str = "Structural diagram"):
    st.markdown(f"**{label}**")
    st.code(diagram, language="text")


def wrapped_text(text: str):
    return "\n".join(textwrap.wrap(text, width=110))


def rec_box(items: list):
    """Render a styled recommendations block."""
    st.markdown("**★ Recommendations**")
    for item in items:
        st.markdown(f"- {item}")


# ---------------------------------------------------------
# Category 1 – FaaS
# ---------------------------------------------------------
def category_1_faas():
    section_header("1. Function-as-a-Service (FaaS)",
                   "Event-driven, stateless functions managed by the cloud provider.")

    st.write(
        "FaaS is the core building block of serverless computing. Developers write small, "
        "single-purpose functions; the platform handles provisioning, scaling, patching, and "
        "billing at millisecond granularity. No servers to manage — ever."
    )

    show_ascii("""
  FaaS CONCEPTUAL ARCHITECTURE

  ┌─────────────────────────────────────────────────────────────────┐
  │                   SERVERLESS PLATFORM                           │
  │                                                                 │
  │  Event Sources        Function Runtime       Outputs            │
  │  ─────────────        ────────────────       ───────            │
  │  HTTP / API  ──────►  [ Function A ]  ──────► Database         │
  │  Queue Msg   ──────►  [ Function B ]  ──────► Object Store     │
  │  Cron / Timer──────►  [ Function C ]  ──────► Event Bus        │
  │  Storage Event─────►  [ Function D ]  ──────► Notification     │
  │  IoT / MQTT  ──────►  [ Function E ]  ──────► Downstream Fn    │
  │                                                                 │
  │  Platform Services: Autoscale │ Billing │ Logs │ Tracing       │
  └─────────────────────────────────────────────────────────────────┘
""", "FaaS Platform Architecture")

    sub_choice = st.radio(
        "Select FaaS capability",
        [
            "Show full capability list",
            "Function execution capability",
            "Storage capability",
            "Container infrastructure capability",
            "Networking capability",
            "Fault tolerance capabilities",
            "Scaling of functions",
            "Data analytics at the edge",
            "Scientific computing",
            "Mobile computing",
        ],
    )

    if sub_choice == "Show full capability list":
        st.markdown("### Full FaaS capability overview")
        st.write(
            "A serverless platform manages the full lifecycle of functions: provisioning, execution, "
            "autoscaling, and teardown. Developers focus exclusively on business logic. Typical real-world "
            "deployments include image processing APIs, webhook handlers, IoT data pipelines, real-time "
            "notification services, and scheduled data transformation jobs."
        )
        st.write(
            "In practice, an e-commerce platform uses FaaS to process payments, send confirmation emails, "
            "update inventory, generate invoices, and log analytics events — each as an independent function "
            "triggered by its own event, scaling independently."
        )
        df = generate_synthetic_faas_data()
        st.markdown("#### Synthetic FaaS workload sample")
        st.dataframe(df, use_container_width=True)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇ Download FaaS workload sample (CSV)", csv, "faas_workload_sample.csv", "text/csv")
        show_mermaid("""
flowchart LR
    UserRequest -->|HTTP/API| API_Gateway
    API_Gateway -->|Invoke| FaaS_Function
    FaaS_Function -->|Read/Write| DataStore[(Object Storage)]
    FaaS_Function --> EventBus((Event Bus))
    EventBus --> OtherFunctions
    OtherFunctions --> AnalyticsDB[(Analytics DB)]
    OtherFunctions --> NotifService((Push Notification))
""", "Full FaaS event flow")
        rec_box([
            "Decompose monolithic services into small, single-purpose functions.",
            "Use an API Gateway (AWS API GW, Azure APIM) in front of all HTTP-triggered functions.",
            "Tag functions by team and cost center for granular billing visibility.",
            "Set per-function memory and timeout limits to avoid runaway costs.",
        ])

    elif sub_choice == "Function execution capability":
        st.markdown("### Function execution capability")
        st.write(
            "Functions are short-lived, stateless compute units triggered by events: HTTP calls, queue messages, "
            "object storage changes, database streams, or cron schedules. The platform spins up micro-VMs or "
            "containers on demand, executes the function, and reclaims resources. Execution time is billed to the "
            "nearest millisecond — you pay only for active CPU time."
        )
        st.write(
            "**Real-world example (Stripe):** Stripe processes billions of payment webhook calls per month using "
            "serverless functions. Each webhook validates the event signature, updates the order database, and "
            "publishes a fulfillment event — all in under 200 ms."
        )
        show_ascii("""
  FUNCTION EXECUTION LIFECYCLE

  Event ──► [Platform Scheduler]
                    │
            ┌───────▼────────┐
            │  Cold Start?   │
            └───┬────────┬───┘
               YES       NO
                │         │
          [Provision]  [Warm Pool]
                │         │
          [Init Runtime]  │
                └────┬────┘
                     ▼
              [Execute Function]
                     │
            ┌────────▼────────┐
            │  Write Outputs  │
            └────────┬────────┘
                     ▼
              [Release / Reclaim Resources]
""", "Function execution lifecycle")
        show_mermaid("""
flowchart LR
    PaymentGateway --> WebhookEndpoint
    WebhookEndpoint --> ValidateFn
    ValidateFn -->|Valid| FaaS_PaymentFn
    ValidateFn -->|Invalid| DLQ((Dead-Letter Queue))
    FaaS_PaymentFn --> OrdersDB[(Orders DB)]
    FaaS_PaymentFn --> FulfillmentQueue((Fulfillment Queue))
    FulfillmentQueue --> ShipFn
""", "Payment webhook function flow")
        rec_box([
            "Keep functions under 50 lines of logic; delegate heavy lifting to libraries or services.",
            "Use provisioned concurrency for latency-sensitive paths to eliminate cold starts.",
            "Validate and sanitize all inputs at the function boundary — never trust the event payload.",
            "Set a realistic timeout (e.g., 10 s for API, 5 min for batch) to cap runaway execution costs.",
        ])

    elif sub_choice == "Storage capability":
        st.markdown("### Storage capability")
        st.write(
            "Since functions are stateless, all durable state lives in external storage: object stores (S3, GCS, "
            "Azure Blob), relational/NoSQL databases, in-memory caches (Redis, Elasticache), or event logs "
            "(Kinesis, Kafka). Intermediate pipeline results flow through object storage, enabling loosely coupled, "
            "independently scalable processing stages."
        )
        st.write(
            "**Real-world example (Netflix):** Netflix uses AWS Lambda with S3 as an intermediary to transcode video "
            "files. Each Lambda reads from S3, processes a chunk, and writes output back — enabling massive parallelism "
            "without managing a transcoding fleet."
        )
        show_ascii("""
  SERVERLESS STORAGE TIERS

  ┌──────────────────────────────────────────────────────┐
  │  Hot Path (ms latency)                               │
  │  Redis / DynamoDB / Cosmos DB ◄── Function reads    │
  ├──────────────────────────────────────────────────────┤
  │  Warm Path (seconds)                                 │
  │  Object Storage (S3 / GCS / Blob) ◄── Intermediate  │
  ├──────────────────────────────────────────────────────┤
  │  Cold Path (minutes)                                 │
  │  Data Warehouse (Redshift / BigQuery / Synapse)      │
  │  ◄── Aggregated / analytical results                 │
  └──────────────────────────────────────────────────────┘
""", "Serverless storage tiers")
        show_mermaid("""
flowchart LR
    RawLogs[(Raw Logs in Object Storage)] --> TransformFn
    TransformFn --> AggregatedMetrics[(Aggregated Metrics DB)]
    AggregatedMetrics --> Dashboard
    TransformFn --> Cache[(Redis Hot Cache)]
    Cache --> RealTimeAPI
""", "Log processing pipeline with tiered storage")
        rec_box([
            "Never store state in function memory across invocations — use external stores.",
            "Use DynamoDB or Cosmos DB for low-latency state; S3 for bulk or intermediate data.",
            "Enable S3 Versioning and lifecycle policies to manage intermediate artifact costs.",
            "Cache frequently read configuration in Redis to avoid repeated database calls.",
        ])

    elif sub_choice == "Container infrastructure capability":
        st.markdown("### Container infrastructure capability")
        st.write(
            "Modern FaaS platforms support container-based functions (AWS Lambda Container Images, Azure Container Apps, "
            "GCP Cloud Run), enabling custom runtimes, larger packages, and specialized tools. OpenFaaS and Knative "
            "run containerized functions on Kubernetes, combining FaaS developer experience with container portability."
        )
        st.write(
            "**Real-world example (Genomics England):** Genomics England runs bioinformatics workflows as containerized "
            "Lambda functions with custom C++ alignment tools. New genomic datasets arriving in S3 automatically trigger "
            "analysis pipelines without provisioning HPC clusters."
        )
        show_ascii("""
  CONTAINER-BASED FaaS STACK

  Developer writes Dockerfile
          │
          ▼
  Container Registry (ECR / ACR / GCR)
          │
          ▼
  FaaS Platform pulls image on cold start
          │
          ▼
  ┌────────────────────────────┐
  │  Micro-VM (Firecracker)    │
  │  └─ Container Runtime      │
  │     └─ Function Code       │
  │        └─ Custom Tools     │
  │           (e.g., GATK,     │
  │            ffmpeg, etc.)   │
  └────────────────────────────┘
""", "Container FaaS runtime stack")
        show_mermaid("""
flowchart LR
    DataBucket[(Genomics Data Bucket)] --> S3Trigger
    S3Trigger --> ContainerFn1[Alignment Container Fn]
    ContainerFn1 --> ContainerFn2[Variant Calling Fn]
    ContainerFn2 --> ContainerFn3[Annotation Fn]
    ContainerFn3 --> ResultsBucket[(Analysis Results Bucket)]
    ResultsBucket --> ReportFn[Report Generator Fn]
""", "Containerized genomics pipeline")
        rec_box([
            "Use container images when your dependency package exceeds the 250 MB zip limit.",
            "Pin container image tags to digests (not 'latest') for reproducible deployments.",
            "Use multi-stage Docker builds to keep images lean and reduce cold start time.",
            "Consider Firecracker-based runtimes (Lambda) for better security isolation vs. shared containers.",
        ])

    elif sub_choice == "Networking capability":
        st.markdown("### Networking capability")
        st.write(
            "Functions can communicate via HTTP/REST, gRPC, event buses (EventBridge, Pub/Sub), message queues "
            "(SQS, Service Bus, Cloud Tasks), and streaming platforms (Kinesis, Kafka). VPC integration allows "
            "functions to access private resources. Service meshes and API gateways enforce policies at the edge."
        )
        st.write(
            "**Real-world example (Delivery Hero):** Delivery Hero uses AWS EventBridge to fan out order events to "
            "dozens of downstream Lambda functions (notifications, inventory, analytics, loyalty) without any "
            "point-to-point coupling between services."
        )
        show_ascii("""
  SERVERLESS NETWORKING PATTERNS

  Pattern 1: Synchronous (HTTP)
  Client ──► API Gateway ──► Function ──► Response

  Pattern 2: Async Fan-out (Event Bus)
  Producer Fn ──► EventBridge ──► Fn A (notify)
                              ──► Fn B (inventory)
                              ──► Fn C (analytics)

  Pattern 3: Queue-based Decoupling
  Fn A ──► SQS Queue ──► Fn B (batch consumer)

  Pattern 4: Streaming
  Kinesis Stream ──► Function (shard consumer)
""", "Serverless networking patterns")
        show_mermaid("""
flowchart LR
    UploadVideo --> SegmenterFn
    SegmenterFn --> SegmentQueue((SQS Segment Queue))
    SegmentQueue --> TranscodeFn1
    SegmentQueue --> TranscodeFn2
    SegmentQueue --> TranscodeFn3
    TranscodeFn1 --> MergeFn
    TranscodeFn2 --> MergeFn
    TranscodeFn3 --> MergeFn
    MergeFn --> FinalVideo[(Final Output Bucket)]
    MergeFn --> NotifyFn((Notify User))
""", "Parallel video transcoding via queue fan-out")
        rec_box([
            "Prefer async (queue/event) communication over synchronous chains to avoid cascading timeouts.",
            "Use VPC endpoints for functions accessing private RDS/Elasticache to avoid public internet exposure.",
            "Implement circuit breakers in functions that call external HTTP APIs.",
            "Use EventBridge schema registry to enforce event contracts between producer and consumer functions.",
        ])

    elif sub_choice == "Fault tolerance capabilities":
        st.markdown("### Fault tolerance capabilities")
        st.write(
            "FaaS platforms provide built-in retry logic, automatic failover to healthy instances, and dead-letter "
            "queues (DLQs) for unprocessable messages. Idempotency is critical: because retries are automatic, "
            "functions must produce the same result when called multiple times with the same input."
        )
        st.write(
            "**Real-world example (Airbnb):** Airbnb's booking confirmation functions are designed to be idempotent "
            "using a transaction ID. If a Lambda retries due to a transient DynamoDB timeout, the second attempt "
            "detects the existing record and skips re-processing — preventing double bookings."
        )
        show_ascii("""
  FAULT TOLERANCE FLOW

  Event arrives
      │
      ▼
  [Function Invoked]
      │
  ┌───▼────────────┐      Success      ┌─────────────┐
  │  Try Execute   │ ────────────────► │  Write to   │
  └───┬────────────┘                   │  DB / Queue │
      │ Failure                        └─────────────┘
      ▼
  [Retry 1] ──► [Retry 2] ──► [Retry N]
      │ All retries exhausted
      ▼
  [Dead-Letter Queue]
      │
  [Alert + Manual Review]
""", "Fault tolerance and retry flow")
        show_mermaid("""
flowchart LR
    IoTDevice --> IngestFn
    IngestFn -->|Success| MetricsDB[(Metrics DB)]
    IngestFn -->|Transient Error| RetryLogic{Retry?}
    RetryLogic -->|Yes - Attempt 2-3| IngestFn
    RetryLogic -->|Exhausted| DLQ((Dead-Letter Queue))
    DLQ --> AlertFn
    AlertFn --> OpsTeam((Ops Alert))
""", "IoT ingestion with retry and DLQ")
        rec_box([
            "Design all functions to be idempotent — use a unique request/transaction ID as a deduplication key.",
            "Configure DLQs on all async event sources (SQS, SNS, EventBridge) and alert on DLQ depth.",
            "Implement exponential backoff with jitter in functions calling external APIs.",
            "Use AWS Step Functions or Azure Durable Functions for complex workflows needing state-aware retries.",
        ])

    elif sub_choice == "Scaling of functions":
        st.markdown("### Scaling of functions")
        st.write(
            "Serverless platforms scale function concurrency automatically from zero to thousands of instances within "
            "seconds. Each invocation runs in an isolated context; the platform manages instance pooling transparently. "
            "Throttling (concurrency limits) prevents downstream services from being overwhelmed."
        )
        st.write(
            "**Real-world example (Coca-Cola):** Coca-Cola's vending machine platform uses AWS Lambda to handle "
            "purchase events. During peak promotions, invocations spike 50x in minutes — Lambda scales horizontally "
            "with zero operator intervention, then scales back to near-zero overnight."
        )
        show_ascii("""
  SERVERLESS AUTO-SCALING

  Traffic:    ░░░░▓▓▓▓▓▓▓▓████████▓▓▓▓░░░░
              Low  Ramp   Peak      Drain  Low

  Instances:  1    10     1000+     50     1
                          │
                    Concurrency Limit
                    (configurable, prevents
                     DB connection exhaustion)
""", "Serverless auto-scaling over time")
        show_mermaid("""
flowchart LR
    Users --> API_Gateway
    API_Gateway --> FaaS_Instances
    subgraph FaaS_Instances [Auto-scaled Function Pool]
        Fn1
        Fn2
        Fn3
        FnN[Fn ... N]
    end
    FaaS_Instances --> RDSProxy[(RDS Proxy - Connection Pool)]
    RDSProxy --> Database[(Database)]
""", "Auto-scaling with RDS Proxy to protect DB connections")
        rec_box([
            "Set reserved concurrency on critical functions to guarantee capacity during traffic spikes.",
            "Use RDS Proxy (AWS) or connection poolers to prevent Lambda from exhausting DB connections at scale.",
            "Implement account-level concurrency quotas awareness — request limit increases proactively.",
            "Monitor concurrency utilization; set CloudWatch alarms when approaching throttle thresholds.",
        ])

    elif sub_choice == "Data analytics at the edge":
        st.markdown("### Data analytics at the network edge")
        st.write(
            "Edge serverless platforms (Cloudflare Workers, AWS Lambda@Edge, Fastly Compute) run functions in "
            "100+ PoPs globally, reducing round-trip latency from hundreds of milliseconds to single digits. "
            "Common workloads: real-time personalization, A/B testing, image optimization, anomaly detection, "
            "and local data aggregation before cloud upload."
        )
        st.write(
            "**Real-world example (Shopify):** Shopify uses Cloudflare Workers at the edge to apply real-time "
            "storefront personalization (currency, language, pricing) without a round-trip to origin servers — "
            "cutting page load time by ~40% for international users."
        )
        show_ascii("""
  EDGE SERVERLESS TOPOLOGY

  User (Tokyo) ──► [PoP: Tokyo] ──► Edge Function
                                         │
                                   Local processing
                                   (auth, personalize,
                                    A/B test, cache)
                                         │
                              ┌──────────▼──────────┐
                              │ Forward only what's  │
                              │ needed to Origin     │
                              └──────────────────────┘
                              Origin (US-East): heavy logic

  Latency: 5 ms at edge vs 180 ms round-trip to origin
""", "Edge vs. origin latency topology")
        show_mermaid("""
flowchart LR
    Camera --> EdgeFn[Edge Detection Fn - PoP]
    EdgeFn -->|No incident| Discard[Discard Frame]
    EdgeFn -->|Incident detected| CloudAnalytics[(Cloud Analytics)]
    EdgeFn --> LocalAlert[(Local Alert Dashboard)]
    CloudAnalytics --> MLModel[Incident Classification]
""", "Smart city edge analytics flow")
        rec_box([
            "Use edge functions for auth, routing, and personalization — not heavy compute.",
            "Store frequently accessed data in edge KV stores (Cloudflare KV, Lambda@Edge + CloudFront) to avoid origin calls.",
            "Design edge functions to be stateless; propagate state to origin or edge KV only.",
            "Monitor edge function CPU time limits (Cloudflare: 50 ms, Lambda@Edge: 5 s) and profile regularly.",
        ])

    elif sub_choice == "Scientific computing":
        st.markdown("### Scientific computing")
        st.write(
            "Scientific workflows often consist of discrete event-driven steps: data ingestion, quality control, "
            "simulation, post-processing, and visualization. Serverless functions orchestrate these steps — triggered "
            "by new data arrivals or completed upstream tasks — without maintaining long-running cluster infrastructure."
        )
        st.write(
            "**Real-world example (NASA JPL):** NASA's Jet Propulsion Laboratory uses AWS Lambda and Step Functions "
            "to process Mars rover telemetry. New data packets arriving in S3 automatically trigger preprocessing, "
            "calibration, and image assembly pipelines — processing years of rover data in weeks of compute."
        )
        show_ascii("""
  SCIENTIFIC WORKFLOW ORCHESTRATION

  [New Data Arrives in Object Store]
            │
            ▼
  [QC / Validation Function]
            │
      ┌─────▼──────┐
      │  Pass QC?  │
      └──┬──────┬──┘
        YES     NO
         │       └──► [Quarantine Bucket]
         ▼
  [Preprocessing Function]
         │
         ▼
  [Simulation / Analysis Function]
  (may fan out to 100s of parallel instances)
         │
         ▼
  [Post-processing + Visualization]
         │
         ▼
  [Results Store + Notification]
""", "Scientific pipeline stages")
        show_mermaid("""
flowchart LR
    SatelliteData[(Satellite Data Bucket)] --> QCFn[QC Validation Fn]
    QCFn -->|Pass| PreprocessFn
    QCFn -->|Fail| Quarantine[(Quarantine Bucket)]
    PreprocessFn --> SimulationFn
    SimulationFn --> ParallelFns
    subgraph ParallelFns [Parallel Simulation Workers]
        Sim1
        Sim2
        SimN[Sim ... N]
    end
    ParallelFns --> PostProcessFn
    PostProcessFn --> Reports[(Reports & Visuals)]
    PostProcessFn --> NotifyFn((Notify Research Team))
""", "Parallel scientific simulation pipeline")
        rec_box([
            "Use AWS Step Functions Map state or Azure Durable Functions fan-out for massively parallel simulations.",
            "Store intermediate results in S3/GCS with meaningful prefixes for easy resumption after failures.",
            "Set function memory based on working set size — more memory = more vCPU in Lambda.",
            "Use spot/preemptible VMs for heavy simulations; FaaS for orchestration and lightweight transforms.",
        ])

    elif sub_choice == "Mobile computing":
        st.markdown("### Mobile computing")
        st.write(
            "Serverless backends are a natural fit for mobile apps: they scale with user growth, require no server "
            "fleet management, and support independent deployment of features. Common patterns include REST/GraphQL "
            "APIs, push notifications, user authentication, in-app purchase processing, and content delivery."
        )
        st.write(
            "**Real-world example (McDonald's):** McDonald's mobile order platform (serving 20M+ orders/month) uses "
            "AWS Lambda for order processing, menu customization, loyalty point calculation, and push notifications — "
            "scaling seamlessly during breakfast and lunch rushes without pre-provisioning."
        )
        show_ascii("""
  MOBILE SERVERLESS BACKEND (BaaS + FaaS)

  Mobile App
      │
      ├──► [Auth Function] ◄── Cognito / Auth0
      │
      ├──► [GraphQL API Function] ──► DynamoDB
      │         │
      │    [Resolver Functions per field]
      │
      ├──► [Purchase Function] ──► Stripe / Apple Pay
      │         │
      │    [Loyalty Points Fn] ──► Points DB
      │
      └──► [Push Notification Fn] ──► FCM / APNS
""", "Mobile BaaS + FaaS architecture")
        show_mermaid("""
flowchart LR
    MobileApp --> AuthFn[Auth / Token Validate Fn]
    AuthFn -->|Authorized| PurchaseAPI
    PurchaseAPI --> PurchaseFn
    PurchaseFn --> PaymentsGateway((Stripe / Apple Pay))
    PurchaseFn --> OrdersDB[(Orders DB)]
    PurchaseFn --> LoyaltyFn[Loyalty Points Fn]
    LoyaltyFn --> PointsDB[(Points DB)]
    PurchaseFn --> PushFn[Push Notification Fn]
    PushFn --> FCM((FCM / APNS))
""", "Mobile purchase + loyalty + notification flow")
        rec_box([
            "Use AWS Amplify, Firebase, or Supabase to accelerate serverless mobile backend setup.",
            "Implement token-based auth (JWT) at every function — never trust client-side claims.",
            "Cache menu/product data at the edge (CloudFront + Lambda@Edge) to reduce mobile API latency.",
            "Use async queues for non-critical operations (analytics, loyalty) to keep the purchase path fast.",
        ])


# ---------------------------------------------------------
# Category 2 – Platforms
# ---------------------------------------------------------
def category_2_platforms():
    section_header("2. Serverless Application Platforms",
                   "Managed environments for deploying and running serverless workloads.")
    st.write(
        "Serverless platforms provide the runtime, event sources, observability, and billing for functions. "
        "Public cloud platforms (AWS Lambda, Azure Functions, GCP Cloud Functions/Run) offer the broadest "
        "ecosystem integration. Open-source alternatives (OpenFaaS, Knative) offer portability and on-premises "
        "deployment at the cost of additional operational overhead."
    )
    st.write(
        "**Real-world example (Capital One):** Capital One migrated its entire data pipeline infrastructure to "
        "AWS Lambda and serverless, eliminating thousands of servers, reducing costs by 70%, and improving "
        "deployment frequency from quarterly releases to multiple deploys per day."
    )

    df = generate_synthetic_serverless_eval_data()
    st.markdown("#### Platform comparison (synthetic evaluation data)")
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Download platform evaluation (CSV)", csv, "serverless_platform_eval.csv", "text/csv")

    show_ascii("""
  PLATFORM SELECTION DECISION TREE

  Is workload event-driven & short-lived (<15 min)?
  ├── YES ──► Consider FaaS (Lambda / Azure Fn / GCP Fn)
  │           Is cold start critical? (<50 ms?)
  │           ├── YES ──► Cloudflare Workers / Lambda SnapStart
  │           └── NO  ──► Standard Lambda / Azure Fn
  └── NO  ──► Is it containerized?
              ├── YES ──► Cloud Run / App Runner / Fargate
              └── NO  ──► Is it on-prem / Kubernetes?
                          ├── YES ──► Knative / OpenFaaS
                          └── NO  ──► Managed Container Service
""", "Platform selection decision tree")

    show_mermaid("""
flowchart LR
    DevCode[Developer Code] --> CI_CD[CI/CD Pipeline]
    CI_CD -->|Deploy| ServerlessPlatform
    subgraph ServerlessPlatform [Serverless Platform]
        Runtime[Language Runtime]
        Scaler[Auto Scaler]
        EventSource[Event Sources]
        Monitor[Logs & Metrics]
    end
    ServerlessPlatform --> Functions[Running Functions]
    Functions --> Logs[(CloudWatch / App Insights)]
    Functions --> Traces[(X-Ray / Jaeger)]
""", "Dev-to-production serverless deployment flow")

    rec_box([
        "Evaluate platforms on cold start, max timeout, pricing model, and ecosystem lock-in risk.",
        "Use an infrastructure-as-code tool (Serverless Framework, Pulumi, Terraform) to stay platform-agnostic.",
        "Build abstraction layers over platform-specific SDKs to ease future platform migrations.",
        "Start with a managed cloud platform; migrate to Knative/OpenFaaS only if portability is a hard requirement.",
    ])


# ---------------------------------------------------------
# Category 3 – AI & DL
# ---------------------------------------------------------
def category_3_ai_dl():
    section_header("3. AI & Deep Learning",
                   "Using serverless for ML inference, pipelines, and lightweight training coordination.")
    st.write(
        "Serverless functions shine in ML pipelines for data preprocessing, feature engineering, model inference "
        "endpoints, and post-processing. GPU-intensive training typically runs on dedicated clusters, but serverless "
        "orchestrates the surrounding workflow and hosts lightweight inference for cost efficiency."
    )
    st.write(
        "**Real-world example (Intuit):** Intuit uses AWS Lambda to host tax advice ML inference endpoints. "
        "When a user submits a tax question, a Lambda function calls a SageMaker endpoint, post-processes the "
        "result, and returns a structured response — all within 300 ms, scaling to millions of tax season requests "
        "without pre-provisioning GPU fleets."
    )

    df = generate_ai_pipeline_data()
    st.markdown("#### Synthetic ML pipeline stage breakdown")
    st.dataframe(df, use_container_width=True)

    show_ascii("""
  SERVERLESS ML PIPELINE ARCHITECTURE

  [New Training Data in S3]
          │
          ▼
  [Preprocess Fn]  ──────────────────────────────►
          │                                       │
  [Feature Engineering Fn]                  [Data Quality
          │                                   Check Fn]
          ▼                                       │
  [Trigger Training Job]                    [Quarantine
  (SageMaker / Vertex AI)                    if Failed]
          │
          ▼
  [Model Evaluation Fn]
          │
    ┌─────▼──────┐
    │ Passes KPIs?│
    └──┬──────┬──┘
      YES     NO
       │       └──► [Rollback to Previous Model]
       ▼
  [Register Model in Registry]
       │
       ▼
  [Inference Fn] ◄── User Request
       │
  [Return Prediction + Log to Feature Store]
""", "End-to-end serverless ML pipeline")

    show_mermaid("""
flowchart LR
    XRayImage[(X-Ray Image Bucket)] --> PreprocessFn[Preprocess Fn]
    PreprocessFn --> FeatureFn[Feature Engineering Fn]
    FeatureFn --> ModelAPI[SageMaker / Vertex AI Endpoint]
    ModelAPI --> InferenceFn[Post-process Inference Fn]
    InferenceFn --> ResultsDB[(Results DB)]
    InferenceFn --> NotifyFn[Notify Clinician Fn]
    InferenceFn --> FeatureStore[(Feature Store - Logging)]
""", "Medical imaging ML inference pipeline")

    rec_box([
        "Use Lambda + SageMaker endpoints for inference; avoid running model weights inside the function zip.",
        "Cache model artifacts in /tmp (up to 10 GB in Lambda) or use EFS mount for large model files.",
        "Implement model versioning and canary deployments for ML inference updates.",
        "Log all predictions to a feature store for model monitoring, drift detection, and retraining triggers.",
        "Use Bedrock (AWS) or Vertex AI (GCP) serverless LLM APIs to avoid hosting your own model infrastructure.",
    ])


# ---------------------------------------------------------
# Category 4 – Use Cases
# ---------------------------------------------------------
def category_4_use_cases():
    section_header("4. Serverless Use Cases",
                   "Patterns and industries where serverless provides the highest ROI.")
    st.write(
        "Serverless is best suited for event-driven, variable-traffic, short-duration workloads where the cost "
        "of idle infrastructure is significant. Strong fits: API backends, data pipelines, IoT ingestion, "
        "scheduled jobs, integration glue, chatbots, and stream processing."
    )

    use_cases = {
        "API Backends": (
            "REST/GraphQL APIs for web and mobile apps. Scale automatically with traffic spikes.",
            "iRobot uses AWS Lambda to handle 60M+ events/day from home robots."
        ),
        "Data Pipelines": (
            "ETL/ELT jobs triggered by data arrivals: CSV → transform → load into data warehouse.",
            "Coca-Cola runs nightly sales data aggregation via Lambda + Glue + Redshift."
        ),
        "IoT Ingestion": (
            "Ingest millions of sensor readings, validate, enrich, and route to storage or analytics.",
            "BP processes oil rig sensor telemetry via Lambda, saving 25% on pipeline infra costs."
        ),
        "Scheduled Tasks": (
            "Cron-style jobs: report generation, database cleanup, cache warming, certificate rotation.",
            "Fintech firms run regulatory report generation via EventBridge + Lambda every morning."
        ),
        "Stream Processing": (
            "Real-time processing of Kinesis/Kafka streams: fraud detection, clickstream analysis.",
            "Capital One uses Lambda stream consumers for real-time fraud scoring on transactions."
        ),
        "Chatbots & Voice": (
            "NLP processing, intent routing, and backend API calls for conversational interfaces.",
            "Domino's Pizza chatbot uses Lambda to process orders from Alexa, web, and mobile."
        ),
    }

    for uc, (desc, example) in use_cases.items():
        with st.expander(f"📌 {uc}"):
            st.write(desc)
            st.info(f"**Example:** {example}")

    show_ascii("""
  USE CASE FIT MATRIX

  Workload Type          │ Serverless Fit │ Reason
  ───────────────────────┼────────────────┼──────────────────────────
  Event-driven API       │   ★★★★★       │ Auto-scales, pay-per-use
  IoT Ingestion          │   ★★★★★       │ Handles burst, no fleet
  Data Pipeline ETL      │   ★★★★☆       │ Good for <15 min stages
  ML Inference           │   ★★★★☆       │ Great if model is small
  Scheduled Batch        │   ★★★★☆       │ No idle cost
  Stream Processing      │   ★★★☆☆       │ Watch partition limits
  Long-running Jobs      │   ★★☆☆☆       │ Timeout constraints
  HPC / GPU Training     │   ★☆☆☆☆       │ Dedicated infra needed
  Microsecond-latency    │   ★☆☆☆☆       │ Cold start incompatible
""", "Serverless use case fit matrix")

    show_mermaid("""
flowchart LR
    EventSource((Shipment Event)) --> IngestFn[Ingest Fn]
    IngestFn --> ValidateFn{Valid Event?}
    ValidateFn -->|Yes| TrackingDB[(Tracking DB)]
    ValidateFn -->|No| DLQ((DLQ))
    TrackingDB --> NotificationFn[Notification Fn]
    NotificationFn --> CustomerApp((Customer Push Notification))
    NotificationFn --> EmailFn[Email Fn]
""", "Logistics event processing use case")

    rec_box([
        "Start with a serverless-first approach for new workloads; migrate to containers if constraints are hit.",
        "Use the fit matrix to objectively evaluate serverless suitability before committing architecture.",
        "Combine serverless (burst events) with containers (steady baseline) in hybrid architectures.",
        "Document the business case: quantify idle infrastructure cost savings vs. managed service overhead.",
    ])


# ---------------------------------------------------------
# Category 5 – Characteristics
# ---------------------------------------------------------
def category_5_characteristics():
    section_header("5. Serverless Characteristics",
                   "Key properties that distinguish serverless from traditional architectures.")

    characteristics = {
        "Event-driven": "Functions execute in response to events, not continuous polling or listening.",
        "Stateless": "No state persists between invocations; all state lives in external stores.",
        "Auto-scaling": "Platform scales from 0 to thousands of concurrent instances automatically.",
        "Fine-grained billing": "Billed per invocation and per millisecond of CPU time — zero cost at idle.",
        "No server management": "No patching, provisioning, capacity planning, or OS management.",
        "Short execution": "Functions are designed for tasks completing in seconds to minutes.",
        "Polyglot": "Functions can be written in Python, Node.js, Java, Go, .NET, Ruby, and more.",
    }

    for char, desc in characteristics.items():
        st.markdown(f"**{char}:** {desc}")

    show_ascii("""
  SERVERLESS vs. TRADITIONAL COMPARISON

  Attribute           │ Traditional VM/Container │ Serverless FaaS
  ────────────────────┼──────────────────────────┼──────────────────────
  Provisioning        │ Manual / IaC             │ Automatic
  Scaling             │ Manual autoscaling rules │ Automatic (platform)
  Idle Cost           │ Paid 24/7                │ $0 at zero traffic
  Patching            │ Team responsibility      │ Platform managed
  Execution Unit      │ Process / Container      │ Function invocation
  State               │ In-memory possible       │ External only
  Deployment Unit     │ Image / Package          │ Function zip / image
  Billing Granularity │ Hours / Minutes          │ Milliseconds
  Cold Start          │ None (always warm)       │ 50 ms – 1 s typical
""", "Serverless vs. traditional architecture comparison")

    show_mermaid("""
flowchart LR
    Events[Event Sources] --> Functions[Stateless Functions]
    Functions --> ExternalState[(Databases / Queues / Storage)]
    ExternalState --> Observability[(Logs / Metrics / Traces)]
    Observability --> Alerts((Ops Alerts))
    Functions --> DownstreamServices[Downstream APIs / Services]
""", "Serverless characteristics in action")

    rec_box([
        "Design functions to be pure: same input → same output, no side effects except explicit writes.",
        "Externalize all configuration (env vars, Parameter Store, Secret Manager) — never hard-code.",
        "Structure function code as: validate → process → respond (or publish event) for consistency.",
        "Use structured logging (JSON) from day one to enable log-based metrics and tracing correlation.",
    ])


# ---------------------------------------------------------
# Category 6 – Challenges
# ---------------------------------------------------------
def category_6_challenges():
    section_header("6. Serverless Challenges",
                   "Limitations, anti-patterns, and operational concerns to address proactively.")

    st.write(
        "Serverless is powerful but introduces unique operational challenges. Understanding them early prevents "
        "costly architectural rework. The most impactful challenges are cold starts, vendor lock-in, observability "
        "across distributed functions, and stateful workflow complexity."
    )

    df = generate_challenge_data()
    st.markdown("#### Challenge severity and mitigation summary")
    st.dataframe(df, use_container_width=True)

    show_ascii("""
  COLD START ANATOMY

  Request arrives for cold function
        │
        ▼
  [Download function package] ──── 50–300 ms
        │
        ▼
  [Start container / micro-VM] ──── 50–200 ms
        │
        ▼
  [Init language runtime] ──────── 50–500 ms (JVM worst)
        │
        ▼
  [Run initialization code] ──────  varies
        │
        ▼
  [Execute handler] ◄── user sees this delay

  Total cold start: 150 ms (Go/Node) to 1000+ ms (Java cold)

  MITIGATIONS:
  ├── Provisioned Concurrency (pre-warm instances)
  ├── Lambda SnapStart (Java: snapshot post-init state)
  ├── Use lighter runtimes (Node.js, Python, Go)
  └── Scheduled warm-up pings (every 5 min)
""", "Cold start anatomy and mitigations")

    show_mermaid("""
flowchart LR
    UserRequest --> ColdStartCheck{Warm Instance Available?}
    ColdStartCheck -->|Yes| WarmPool[(Warm Instance Pool)]
    ColdStartCheck -->|No - Cold Start| Provision[Provision + Init]
    Provision --> FunctionExec[Execute Handler]
    WarmPool --> FunctionExec
    FunctionExec --> Response[Return Response]
    FunctionExec --> KeepWarm[Instance stays warm briefly]
""", "Cold start decision flow")

    show_ascii("""
  OBSERVABILITY CHALLENGE IN SERVERLESS

  Traditional: 1 process → 1 log stream → easy correlation
  Serverless:  1000 concurrent functions → 1000 log streams
               Each invocation has unique request ID
               Traces span Lambda → SQS → Lambda → DynamoDB

  SOLUTION STACK:
  ├── Structured JSON logs with correlation ID
  ├── AWS X-Ray / Azure Application Insights distributed tracing
  ├── OpenTelemetry for vendor-neutral instrumentation
  └── Observability platforms: Honeycomb, Datadog, Lumigo, Epsagon
""", "Observability challenge and solution")

    rec_box([
        "Use provisioned concurrency for latency-sensitive production paths; benchmark cost vs. cold start impact.",
        "Adopt OpenTelemetry from day one — instrument all functions with traces, metrics, and logs.",
        "Use Serverless Framework or SST to abstract platform differences and reduce lock-in surface area.",
        "Avoid long function chains (>3 hops sync); switch to event-driven async for complex workflows.",
        "Test locally with LocalStack (AWS) or Azurite (Azure) before deploying to cloud.",
    ])


# ---------------------------------------------------------
# Category 7 – Evaluation Criteria
# ---------------------------------------------------------
def category_7_evaluation():
    section_header("7. Serverless Evaluation Criteria",
                   "How to rigorously assess platforms, architectures, and trade-offs.")

    st.write(
        "Choosing a serverless platform is a strategic decision with long-term implications. Evaluation should be "
        "data-driven, covering performance benchmarks, cost modeling, ecosystem maturity, security, and migration risk."
    )

    df = generate_synthetic_serverless_eval_data()
    st.markdown("#### Platform benchmark comparison")
    st.dataframe(df, use_container_width=True)

    show_ascii("""
  EVALUATION FRAMEWORK (Weighted Scorecard)

  Criterion              │ Weight │ AWS Lambda │ Azure Fn │ GCP Fn │ OpenFaaS
  ───────────────────────┼────────┼────────────┼──────────┼────────┼──────────
  Cold Start Latency     │  20%   │    ★★★★    │   ★★★    │  ★★★★  │   ★★
  Max Execution Time     │  10%   │    ★★★★★   │  ★★★★    │  ★★★   │  ★★★
  Ecosystem / Triggers   │  20%   │    ★★★★★   │  ★★★★    │  ★★★★  │   ★★
  Pricing (per req)      │  15%   │    ★★★★    │  ★★★★    │ ★★★★★  │   ★★★
  Vendor Lock-in Risk    │  15%   │    ★★       │   ★★     │   ★★   │ ★★★★★
  Security & Compliance  │  10%   │    ★★★★★   │ ★★★★★   │  ★★★★  │   ★★★
  Observability Built-in │  10%   │    ★★★★    │  ★★★★    │  ★★★   │   ★★
""", "Weighted evaluation scorecard")

    show_mermaid("""
flowchart LR
    Workload[Define Workload Characteristics] --> BenchmarkSuite[Build Benchmark Suite]
    BenchmarkSuite --> PlatformA[AWS Lambda]
    BenchmarkSuite --> PlatformB[Azure Functions]
    BenchmarkSuite --> PlatformC[GCP Cloud Functions]
    PlatformA --> MetricsA[(Latency / Cost / Limits)]
    PlatformB --> MetricsB[(Latency / Cost / Limits)]
    PlatformC --> MetricsC[(Latency / Cost / Limits)]
    MetricsA --> Scorecard[Weighted Scorecard]
    MetricsB --> Scorecard
    MetricsC --> Scorecard
    Scorecard --> Decision[Platform Decision]
""", "Platform evaluation process flow")

    rec_box([
        "Run benchmarks with YOUR workload — cold start numbers vary dramatically by runtime and package size.",
        "Model cost at 3 traffic scenarios: baseline, 2x peak, and 10x spike. Serverless can be expensive at extreme scale.",
        "Evaluate integration depth: does the platform natively support your event sources (Kafka, RabbitMQ, custom)?",
        "Score vendor lock-in risk by counting platform-specific APIs — the fewer, the more portable your code.",
        "Include security criteria: VPC support, secrets management, IAM granularity, and compliance certifications.",
    ])


# ---------------------------------------------------------
# Category 8 – Gaps & Limitations
# ---------------------------------------------------------
def category_8_gaps():
    section_header("8. Serverless Gaps & Limitations",
                   "Where serverless is not yet ideal — and hybrid strategies to address gaps.")

    st.write(
        "Serverless is not a universal solution. Specific workloads are poorly served by current FaaS platforms: "
        "microsecond-latency systems, long-running compute jobs, heavy stateful applications, and workloads with "
        "strict GPU/networking requirements. Understanding these gaps enables hybrid architectures that use "
        "serverless where it excels and dedicated infrastructure where it doesn't."
    )
    st.write(
        "**Real-world example (High-Frequency Trading):** A trading firm evaluated Lambda for order execution but "
        "found P99 latency of 8 ms unacceptable (requirement: <500 µs). They use co-located bare-metal servers for "
        "execution and Lambda only for non-critical auxiliary tasks (reporting, notifications)."
    )

    show_ascii("""
  SERVERLESS SUITABILITY RADAR

  Workload                │ Serverless │ Container │ Bare Metal / VM
  ────────────────────────┼────────────┼───────────┼─────────────────
  Event-driven bursts     │   BEST     │   Good    │   Poor (oversize)
  API backend (variable)  │   BEST     │   Good    │   Poor
  Long-running batch      │   Poor     │   BEST    │   Good
  Stateful services       │   Poor     │   BEST    │   Good
  GPU/ML training         │   Poor     │   Good    │   BEST
  Microsecond latency     │   Poor     │   Good    │   BEST
  Complex networking      │   Poor     │   Good    │   BEST
  Steady high-volume      │   Costly   │   BEST    │   Good
""", "Workload suitability radar")

    show_mermaid("""
flowchart LR
    Requirements[Workload Requirements] --> FitCheck{Serverless Fit?}
    FitCheck -->|Event-driven, short, variable| Serverless[FaaS - Lambda / Fn]
    FitCheck -->|Containerized, moderate duration| Container[Cloud Run / Fargate]
    FitCheck -->|Long-running, stateful| DedicatedVM[VMs / Bare Metal]
    FitCheck -->|GPU-intensive| GPU[GPU Cluster / SageMaker]
    Serverless --> Monitor[Monitor + Re-evaluate Quarterly]
    Container --> Monitor
    DedicatedVM --> Monitor
    GPU --> Monitor
""", "Workload-to-infrastructure routing decision")

    show_ascii("""
  HYBRID ARCHITECTURE PATTERN

  ┌──────────────────────────────────────────────────────────┐
  │                  HYBRID CLOUD ARCHITECTURE               │
  │                                                          │
  │  Serverless Layer (FaaS)                                 │
  │  ├── API Gateway + Lambda  ← Variable user traffic       │
  │  ├── Event processors      ← IoT / webhook bursts        │
  │  └── Scheduled tasks       ← Low-frequency cron jobs     │
  │                                                          │
  │  Container Layer (steady baseline)                       │
  │  ├── Core microservices    ← Sustained request rate      │
  │  └── ML inference servers  ← Warm model, low latency     │
  │                                                          │
  │  Dedicated Infrastructure                                │
  │  ├── GPU training clusters ← Model training jobs         │
  │  └── HPC / bare metal      ← Latency-critical compute    │
  └──────────────────────────────────────────────────────────┘
""", "Hybrid architecture combining serverless, containers, and dedicated infra")

    rec_box([
        "Map workload requirements (latency, duration, state, GPU) before choosing execution model.",
        "Use serverless for orchestration and glue even when compute uses dedicated infra.",
        "Re-evaluate architecture fit annually — platform limits (timeout, memory, networking) improve over time.",
        "Design abstraction layers so compute backends can be swapped without rewriting business logic.",
        "Track serverless spend monthly; switch to containers for workloads with >500 hrs/month steady execution.",
    ])


# ---------------------------------------------------------
# Main app
# ---------------------------------------------------------
def main():
    st.set_page_config(
        page_title="Serverless Computing Framework",
        page_icon="⚙️",
        layout="wide",
    )

    # Bold blue title + blue developer credit
    st.markdown(
        """
        <h1 style='color:#1a5fb4; font-weight:900; margin-bottom:4px;'>
            ⚙️ Serverless Computing Framework Application
        </h1>
        <p style='color:#1a5fb4; font-size:15px; margin-top:0; margin-bottom:16px;'>
            Developed by <strong>Randy Singh</strong> &mdash;
            <em>Kalsnet (KNet) Consulting Group</em>
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "> Recent advancements in virtualization and software architecture have led to serverless computing, "
        "where applications run as stateless functions managed entirely by the platform — no servers to provision, "
        "patch, or scale. This dashboard covers all eight framework categories with detailed guidance, "
        "real-world examples, structural diagrams, and actionable recommendations."
    )

    st.sidebar.title("Framework Main Menu")
    category = st.sidebar.selectbox(
        "Select framework category (1–8)",
        [
            "1. Function-as-Service (FaaS)",
            "2. Serverless application platforms",
            "3. AI & deep learning",
            "4. Serverless use cases",
            "5. Serverless characteristics",
            "6. Serverless challenges",
            "7. Serverless evaluation criteria",
            "8. Serverless gaps & limitations",
        ],
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Export & synthetic data**")
    st.sidebar.markdown(
        "Each category includes synthetic datasets, CSV exports, Mermaid flow diagrams, "
        "and ASCII structural diagrams."
    )
    st.sidebar.markdown("---")
    st.sidebar.caption("Kalsnet (KNet) Consulting Group · Randy Singh")

    if category.startswith("1."):
        category_1_faas()
    elif category.startswith("2."):
        category_2_platforms()
    elif category.startswith("3."):
        category_3_ai_dl()
    elif category.startswith("4."):
        category_4_use_cases()
    elif category.startswith("5."):
        category_5_characteristics()
    elif category.startswith("6."):
        category_6_challenges()
    elif category.startswith("7."):
        category_7_evaluation()
    elif category.startswith("8."):
        category_8_gaps()

    st.markdown("---")
    st.caption(
        "Serverless Computing Framework Dashboard · Developed by Randy Singh, "
        "Kalsnet (KNet) Consulting Group · "
        "Based on current industry best practices and cloud provider documentation."
    )


if __name__ == "__main__":
    main()

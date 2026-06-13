# Serverless Computing Framework

import streamlit as st
import pandas as pd
import textwrap
from io import StringIO

# ---------------------------------------------------------
# Helper: synthetic data generator for export/demo
# ---------------------------------------------------------
def generate_synthetic_faas_data():
    data = {
        "FunctionName": [
            "image_resize",
            "log_aggregator",
            "payment_webhook",
            "iot_sensor_ingest",
            "video_transcode_chunk",
        ],
        "TriggerType": [
            "HTTP API",
            "Log Event",
            "Webhook",
            "MQTT Message",
            "Object Storage Event",
        ],
        "AvgExecTime_ms": [120, 35, 210, 80, 950],
        "MonthlyInvocations": [50000, 120000, 15000, 250000, 8000],
        "CloudProvider": [
            "AWS Lambda",
            "Azure Functions",
            "GCP Cloud Functions",
            "AWS Lambda",
            "Cloudflare Workers",
        ],
    }
    return pd.DataFrame(data)


def generate_synthetic_serverless_eval_data():
    data = {
        "Platform": [
            "AWS Lambda",
            "Azure Functions",
            "GCP Cloud Functions",
            "OpenFaaS",
            "Knative",
        ],
        "ColdStart_ms": [350, 420, 380, 600, 700],
        "MaxConcurrent": [1000, 800, 900, 500, 400],
        "PricingModel": [
            "per-ms",
            "per-ms",
            "per-ms",
            "per-node",
            "per-node",
        ],
        "BestFor": [
            "Event-driven APIs",
            "Enterprise integrations",
            "Data pipelines",
            "On-prem FaaS",
            "Kubernetes-native apps",
        ],
    }
    return pd.DataFrame(data)


# ---------------------------------------------------------
# Layout helpers
# ---------------------------------------------------------
def section_header(title: str, subtitle: str = ""):
    st.markdown(f"## {title}")
    if subtitle:
        st.caption(subtitle)


def show_mermaid_diagram(diagram_code: str):
    st.markdown("#### Conceptual flow")
    st.markdown("```mermaid\n" + diagram_code + "\n```")


def wrapped_text(text: str):
    return "\n".join(textwrap.wrap(text, width=100))


# ---------------------------------------------------------
# Category content functions
# ---------------------------------------------------------
def category_1_faas():
    section_header("1. Function-as-a-Service (FaaS)", "Event-driven, stateless functions managed by the cloud provider.")

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

    # Real-world examples + explanations
    if sub_choice == "Show full capability list":
        st.markdown("### Full FaaS capability overview")
        st.write(
            wrapped_text(
                "A serverless platform manages the lifecycle, execution, and scaling of functions. "
                "Developers focus on business logic while the platform handles provisioning, autoscaling, "
                "and fault isolation. Typical examples include image processing APIs, webhook handlers, "
                "IoT ingestion pipelines, and real-time notification services."
            )
        )
        st.write(
            wrapped_text(
                "In practice, an e-commerce site might use FaaS to process payments, send confirmation emails, "
                "update inventory, and log analytics events—each as separate functions triggered by events."
            )
        )

        df = generate_synthetic_faas_data()
        st.markdown("#### Synthetic FaaS workload sample")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download FaaS workload sample (CSV)",
            csv,
            "faas_workload_sample.csv",
            "text/csv",
        )

        show_mermaid_diagram(
            """
flowchart LR
    UserRequest -->|HTTP/API| API_Gateway
    API_Gateway -->|Invoke| FaaS_Function
    FaaS_Function -->|Read/Write| DataStore[(Object Storage)]
    FaaS_Function --> EventBus((Event Bus))
    EventBus --> OtherFunctions
    OtherFunctions --> AnalyticsDB[(Analytics DB)]
"""
        )

    elif sub_choice == "Function execution capability":
        st.markdown("### Function execution capability")
        st.write(
            wrapped_text(
                "Functions are short-lived, stateless units of computation triggered by events such as HTTP calls, "
                "queue messages, object storage changes, or cron schedules. The platform spins up containers or "
                "micro-VMs on demand, executes the function, and tears down resources after completion."
            )
        )
        st.write(
            wrapped_text(
                "Example: A payment webhook function validates a transaction, writes it to a database, and publishes "
                "an event to trigger downstream fulfillment workflows."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    PaymentGateway --> WebhookEndpoint
    WebhookEndpoint --> FaaS_PaymentFn
    FaaS_PaymentFn --> OrdersDB[(Orders DB)]
    FaaS_PaymentFn --> FulfillmentQueue((Fulfillment Queue))
"""
        )

    elif sub_choice == "Storage capability":
        st.markdown("### Storage capability")
        st.write(
            wrapped_text(
                "Serverless analytics often rely on shared storage such as object stores (e.g., S3), in-memory key-value "
                "stores, or distributed flash storage. Each stage of a pipeline reads and writes intermediate results "
                "to these stores, enabling loosely coupled, scalable processing."
            )
        )
        st.write(
            wrapped_text(
                "Example: A log processing pipeline stores raw logs in object storage, uses functions to transform them, "
                "and writes aggregated metrics to a time-series database."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    RawLogs[(Raw Logs in Object Storage)] --> TransformFn
    TransformFn --> AggregatedMetrics[(Aggregated Metrics)]
    AggregatedMetrics --> Dashboard
"""
        )

    elif sub_choice == "Container infrastructure capability":
        st.markdown("### Container infrastructure capability")
        st.write(
            wrapped_text(
                "Some platforms allow packaging functions as containers, enabling custom runtimes and scientific tools. "
                "Frameworks like SCAR or OpenFaaS run container-based workloads on top of FaaS, making it easier to "
                "bring specialized libraries and languages."
            )
        )
        st.write(
            wrapped_text(
                "Example: A genomics workflow runs containerized functions with specialized bioinformatics tools, "
                "triggered by new data arriving in a research bucket."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    DataBucket[(Genomics Data)] --> Trigger
    Trigger --> ContainerFn1
    ContainerFn1 --> ContainerFn2
    ContainerFn2 --> ResultsBucket[(Analysis Results)]
"""
        )

    elif sub_choice == "Networking capability":
        st.markdown("### Networking capability")
        st.write(
            wrapped_text(
                "Peer-to-peer networking between functions enables streaming, sharing in-memory objects, and complex "
                "distributed algorithms. With serverless networking, functions can communicate directly or via "
                "lightweight channels without always persisting to storage."
            )
        )
        st.write(
            wrapped_text(
                "Example: A video transcoding pipeline uses multiple functions to process segments in parallel, "
                "coordinating via a lightweight messaging layer to assemble the final output."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    UploadVideo --> SegmenterFn
    SegmenterFn --> SegmentQueue((Segment Queue))
    SegmentQueue --> TranscodeFn1
    SegmentQueue --> TranscodeFn2
    TranscodeFn1 --> MergeFn
    TranscodeFn2 --> MergeFn
    MergeFn --> FinalVideo[(Final Output)]
"""
        )

    elif sub_choice == "Fault tolerance capabilities":
        st.markdown("### Fault tolerance capabilities")
        st.write(
            wrapped_text(
                "FaaS platforms typically provide retry-based fault tolerance, automatic isolation of failing instances, "
                "and graceful degradation. Failed invocations can be retried, sent to dead-letter queues, or logged "
                "for later analysis."
            )
        )
        st.write(
            wrapped_text(
                "Example: An IoT ingestion function retries transient network errors and sends malformed messages to a "
                "dead-letter topic for manual inspection."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    IoTDevice --> IngestFn
    IngestFn -->|Success| MetricsDB[(Metrics DB)]
    IngestFn -->|Failure| RetryLogic
    RetryLogic --> DeadLetterQueue((DLQ))
"""
        )

    elif sub_choice == "Scaling of functions":
        st.markdown("### Scaling of functions")
        st.write(
            wrapped_text(
                "Serverless platforms automatically scale functions horizontally based on incoming load. Developers do "
                "not manage autoscaling groups; instead, concurrency limits and throttling policies control behavior."
            )
        )
        st.write(
            wrapped_text(
                "Example: A flash sale API scales from a few requests per second to thousands, with the platform "
                "spawning additional function instances to handle the surge."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    Users --> API_Gateway
    API_Gateway --> FaaS_Instances
    subgraph FaaS_Instances
        Fn1
        Fn2
        Fn3
        FnN
    end
    FaaS_Instances --> OrdersDB[(Orders DB)]
"""
        )

    elif sub_choice == "Data analytics at the edge":
        st.markdown("### Data analytics at the network edge")
        st.write(
            wrapped_text(
                "Edge serverless platforms run functions close to devices, reducing latency and bandwidth usage. "
                "Real-time video analytics, anomaly detection, and local aggregation are common edge workloads."
            )
        )
        st.write(
            wrapped_text(
                "Example: Cameras in a smart city send frames to edge functions that detect incidents and only forward "
                "alerts and metadata to the central cloud."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    Camera --> EdgeFn
    EdgeFn --> LocalAlert[(Local Alert)]
    EdgeFn --> CloudAnalytics[(Cloud Analytics)]
"""
        )

    elif sub_choice == "Scientific computing":
        st.markdown("### Scientific computing")
        st.write(
            wrapped_text(
                "Scientific workflows often consist of event-driven steps: data acquisition, preprocessing, simulation, "
                "and post-processing. Serverless functions can orchestrate these steps, triggered by new datasets or "
                "completed simulations."
            )
        )
        st.write(
            wrapped_text(
                "Example: A climate modeling pipeline triggers simulations when new satellite data arrives, then runs "
                "post-processing functions to generate visualizations and reports."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    SatelliteData[(Satellite Data)] --> PreprocessFn
    PreprocessFn --> SimulationFn
    SimulationFn --> PostProcessFn
    PostProcessFn --> Reports[(Reports & Visuals)]
"""
        )

    elif sub_choice == "Mobile computing":
        st.markdown("### Mobile computing")
        st.write(
            wrapped_text(
                "Hybrid mobile apps can use serverless backends for authentication, purchases, notifications, and "
                "content delivery. Functions scale automatically with user growth and can be updated independently."
            )
        )
        st.write(
            wrapped_text(
                "Example: A mobile shopping app triggers a purchase function when the user taps 'Buy', which records "
                "the order, charges the card, and sends a push notification."
            )
        )
        show_mermaid_diagram(
            """
flowchart LR
    MobileApp --> PurchaseAPI
    PurchaseAPI --> PurchaseFn
    PurchaseFn --> PaymentsGateway
    PurchaseFn --> OrdersDB[(Orders DB)]
    PurchaseFn --> PushService((Push Notification))
"""
        )


def category_2_platforms():
    section_header("2. Serverless application platforms", "Managed environments for deploying and running serverless workloads.")
    st.write(
        wrapped_text(
            "Serverless platforms include public cloud offerings (AWS Lambda, Azure Functions, GCP Cloud Functions) "
            "and open-source frameworks (OpenFaaS, Knative). They provide runtimes, event sources, logging, and "
            "observability out of the box."
        )
    )
    st.write(
        wrapped_text(
            "Real-world example: A healthcare startup uses Azure Functions with Event Grid to process HL7/FHIR messages, "
            "trigger workflows, and integrate with EHR systems without managing servers."
        )
    )

    df = generate_synthetic_serverless_eval_data()
    st.markdown("#### Platform comparison (synthetic evaluation data)")
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download platform evaluation sample (CSV)",
        csv,
        "serverless_platform_eval.csv",
        "text/csv",
    )

    show_mermaid_diagram(
        """
flowchart LR
    DevCode --> CI_CD
    CI_CD --> ServerlessPlatform
    ServerlessPlatform --> Functions
    Functions --> Logs[(Logs & Metrics)]
"""
    )


def category_3_ai_dl():
    section_header("3. AI & deep learning", "Using serverless for ML inference, lightweight training, and pipelines.")
    st.write(
        wrapped_text(
            "Serverless functions can host ML inference endpoints, pre/post-processing steps, and orchestration logic. "
            "Heavy training typically runs on dedicated GPU clusters, but serverless can coordinate data preparation "
            "and model deployment."
        )
    )
    st.write(
        wrapped_text(
            "Example: A dental practice management system uses a serverless function to classify X-ray images via a "
            "hosted model API, then stores results and triggers follow-up workflows."
        )
    )
    show_mermaid_diagram(
        """
flowchart LR
    XRayImage --> PreprocessFn
    PreprocessFn --> ModelAPI
    ModelAPI --> InferenceFn
    InferenceFn --> ResultsDB[(Results DB)]
    InferenceFn --> NotificationService
"""
    )


def category_4_use_cases():
    section_header("4. Serverless use cases", "Patterns where serverless is a strong fit.")
    st.write(
        wrapped_text(
            "Common use cases include API backends, data processing pipelines, IoT ingestion, scheduled tasks, "
            "chatbots, and integration glue between SaaS systems."
        )
    )
    st.write(
        wrapped_text(
            "Example: A logistics company uses serverless functions to process shipment events, update tracking status, "
            "and send notifications to customers in real time."
        )
    )
    show_mermaid_diagram(
        """
flowchart LR
    EventSource((Shipment Event)) --> IngestFn
    IngestFn --> TrackingDB[(Tracking DB)]
    IngestFn --> NotificationFn
    NotificationFn --> CustomerApp
"""
    )


def category_5_characteristics():
    section_header("5. Serverless characteristics", "Key properties that distinguish serverless from traditional architectures.")
    st.write(
        wrapped_text(
            "Core characteristics include: event-driven execution, stateless functions, automatic scaling, fine-grained "
            "billing, and reduced operational overhead. Developers trade control over infrastructure for speed and agility."
        )
    )
    st.write(
        wrapped_text(
            "Example: A startup launches a new feature as a set of functions without provisioning servers, paying only "
            "for actual invocations during beta testing."
        )
    )
    show_mermaid_diagram(
        """
flowchart LR
    Events --> Functions
    Functions --> Services[(Databases, Queues, Storage)]
    Services --> Observability[(Logs, Metrics, Traces)]
"""
    )


def category_6_challenges():
    section_header("6. Serverless challenges", "Limitations and operational concerns.")
    st.write(
        wrapped_text(
            "Challenges include cold starts, vendor lock-in, debugging distributed flows, limited execution time, and "
            "complexity in state management. Observability and testing across many small functions can be difficult."
        )
    )
    st.write(
        wrapped_text(
            "Example: A real-time trading system may struggle with cold start latency and choose a hybrid approach with "
            "long-lived services for critical paths and serverless for auxiliary tasks."
        )
    )
    show_mermaid_diagram(
        """
flowchart LR
    UserRequest --> ColdStartCheck
    ColdStartCheck --> WarmPool[(Warm Instances)]
    ColdStartCheck --> NewInstance[(New Instance)]
    NewInstance --> FunctionExec
"""
    )


def category_7_evaluation():
    section_header("7. Serverless evaluation criteria", "How to assess platforms and architectures.")
    st.write(
        wrapped_text(
            "Evaluation criteria include performance (latency, throughput), scalability, cost, ecosystem maturity, "
            "security features, and integration options. Benchmarks often compare cold start times, sustained load, "
            "and cost per million invocations."
        )
    )
    st.write(
        wrapped_text(
            "Example: A team evaluates AWS Lambda vs. Azure Functions by running the same workload—image processing, "
            "API calls, and database writes—and comparing latency and monthly cost."
        )
    )
    show_mermaid_diagram(
        """
flowchart LR
    Workload --> BenchmarkSuite
    BenchmarkSuite --> PlatformA
    BenchmarkSuite --> PlatformB
    PlatformA --> MetricsA[(Latency, Cost)]
    PlatformB --> MetricsB[(Latency, Cost)]
"""
    )


def category_8_gaps():
    section_header("8. Serverless gaps & limitations", "Where serverless is not yet ideal.")
    st.write(
        wrapped_text(
            "Gaps include limited support for long-running tasks, complex networking topologies, heavy stateful workloads, "
            "and strict latency SLAs. Some organizations also face compliance or data residency constraints."
        )
    )
    st.write(
        wrapped_text(
            "Example: A high-frequency trading engine requires microsecond-level latency and deterministic performance, "
            "which is better served by specialized infrastructure rather than FaaS."
        )
    )
    show_mermaid_diagram(
        """
flowchart LR
    Requirements --> FitCheck
    FitCheck -->|Good Fit| Serverless
    FitCheck -->|Poor Fit| DedicatedInfra[(Dedicated Infrastructure)]
"""
    )


# ---------------------------------------------------------
# Main Streamlit app
# ---------------------------------------------------------
def main():
    st.set_page_config(
        page_title="Serverless Computing Framework",
        page_icon="⚙️",
        layout="wide",
    )

    st.title("Serverless Computing Framework Application")
    st.caption(
        "Recent advancements in virtualization and software architecture have led to serverless computing, "
        "where applications run as stateless functions managed by the platform."
    )

    st.sidebar.title("Framework main menu")
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
        "Each category may include synthetic datasets and CSV export buttons for experimentation."
    )

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


if __name__ == "__main__":
    main()
